---
symbol: "RALBP1"
type: "gene"
col: 303
ensembl_id: "ENSG00000017797"
name: "ralA binding protein 1"
location: "18p11.22"
module: 76
arm: "+"
pooled_cpm: 120.95
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# RALBP1

*ralA binding protein 1* — 18p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.67× (z +6.4, q 5e-08, up in 37 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Osimertinib (mesylate) (drug)]] 5 µM: 1.36× (z +4.8, q 3e-04, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.559× (z -12.5, q 3e-33, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MARCHF8]] (+0.72, fdr 7e-06), [[CCDC28A]] (+0.68, fdr 7e-06), [[WIPI2]] (+0.67, fdr 7e-06); moves opposite to [[THOC6]] (-0.59, fdr 2e-05), [[P2RY11]] (-0.59, fdr 1e-05), [[ERCC6L2]] (-0.58, fdr 1e-04).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 303.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +6.4 | 5e-08 | 37/49 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.4 | 5e-08 | 34/44 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.36×** | +4.8 | 3e-04 | 41/48 (SW1417, C-33 A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.34×** | +4.5 | 8e-04 | 34/48 (AsPC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +4.3 | 0.002 | 28/48 (SW1417, PANC-1, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.29×** | +3.9 | 0.009 | 30/49 (SW1417, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.012 | 32/48 (SW1417, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.061 | 26/48 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.22× | +3.1 | 0.13 | 27/48 (RPMI-7951, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 303.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.559×** | -12.5 | 3e-33 | 43/48 (A-427, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.592×** | -8.0 | 3e-13 | 40/48 (A-427, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.592×** | -8.0 | 3e-13 | 44/48 (NCI-H2347, MIA PaCa-2, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.752×** | -4.3 | 0.002 | 28/48 (A-427, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.773×** | -3.9 | 0.011 | 28/48 (LOX-IMVI, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.799×** | -3.4 | 0.065 | 27/48 (HCT15, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.863× | -3.1 | 0.13 | 10/48 (SW48, HT-29, …) | all doses, flat |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.806× | -3.0 | 0.16 | 23/48 (LoVo, NCI-H2347, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | 0.685× | -3.0 | 0.16 | 20/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 303. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 103 | 3 (2 ⚠) | 2 | [[Selinexor (drug)]] 5 µM 1.86× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 170 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.40× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -15.3) |
| [[NCI-H1573 (line)]] | alt | 101 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.86× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -12.9) |
| [[SW1417 (line)]] | alt | 147 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +12.5) | — |
| [[NCI-H2030 (line)]] | alt | 123 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -16.8) |
| [[SK-MEL-2 (line)]] | alt | 131 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -16.2) |
| [[SW48 (line)]] | wt | 141 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -10.0) |
| [[A-427 (line)]] | wt | 301 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -22.9) |
| [[AsPC-1 (line)]] | alt | 135 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -10.2) |
| [[HOP62 (line)]] | alt | 213 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -21.0) |
| [[hTERT-HPNE (line)]] | wt | 132 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.319× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 126 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -15.4) |
| [[NCI-H23 (line)]] | alt | 174 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 69.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -14.4) |
| [[A549 (line)]] | wt | 83.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 43.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -9.5) |
| [[HCT15 (line)]] | alt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.486× (z -8.5) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 106 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -14.5) |
| [[Hs 766T (line)]] | wt | 116 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -13.7) |
| [[HT-29 (line)]] | alt | 168 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -11.8) |
| [[J82 (line)]] | alt | 99.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -10.5) |
| [[LoVo (line)]] | wt | 104 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 168 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.405× (z -13.1) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 120 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -10.7) |
| [[SNU-423 (line)]] | alt | 92.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -14.4) |
| [[SW 1088 (line)]] | alt | 79.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0817× (z -9.5) |
| [[A-172 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 71.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 149 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 105 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 71.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 92.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 118 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 126 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 94.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 124 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 303), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARCHF8]] | +0.72 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[CCDC28A]] | +0.68 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[WIPI2]] | +0.67 | +0.73 / +0.61 | both halves | 7e-06 | STRING 457 |
| [[MKRN1]] | +0.66 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[FBXL20]] | +0.65 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[TFDP2]] | +0.64 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[KLHL7]] | +0.64 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[NTAN1]] | +0.63 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[MACO1]] | +0.63 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[HEBP2]] | +0.63 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[YPEL2]] | +0.63 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[ZNHIT3]] | +0.62 | +0.47 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC6]] | -0.59 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[P2RY11]] | -0.59 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.58 | -0.65 / -0.34 | both halves | 1e-04 |  |
| [[AFG3L1P]] | -0.57 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[ST7L]] | -0.56 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[CHTOP]] | -0.56 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[ANAPC7]] | -0.54 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[CYREN]] | -0.54 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[MLH1]] | -0.54 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[HNRNPL]] | -0.53 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[POGLUT1]] | -0.53 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[NUP188]] | -0.53 | -0.53 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.749). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.5, -45.1); signed map (-20.1, 9.7). **Vector** length 116, 39.0% of its response variance represented; |z| ≥ 3 in 735 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.6 | +4.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.9 | +3.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +2.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.0 | +3.3 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +4.4 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.1 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | +2.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.3 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.4 | -8.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.3 | -8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.3 | -12.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.6 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.6 | -2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.4 | -2.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | ralA binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.22 — chr18:9,475,009-9,538,114 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RLIP76, RIP1, RIP |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 5 pathways, smallest: CDC42 GTPase cycle; RAC1 GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15311](https://www.uniprot.org/uniprotkb/Q15311) (RalA-binding protein 1):

> Multifunctional protein that functions as a downstream effector of RALA and RALB. As a GTPase-activating protein/GAP can inactivate CDC42 and RAC1 by stimulating their GTPase activity. As part of the Ral signaling pathway, may also regulate ligand-dependent EGF and insulin receptors-mediated endocytosis. During mitosis, may act as a scaffold protein in the phosphorylation of EPSIN/EPN1 by the mitotic kinase cyclin B-CDK1, preventing endocytosis during that phase of the cell cycle. During …

**Summary**, from NCBI Gene [10928](https://www.ncbi.nlm.nih.gov/gene/10928):

> RALBP1 plays a role in receptor-mediated endocytosis and is a downstream effector of the small GTP-binding protein RAL (see RALA; MIM 179550). Small G proteins, such as RAL, have GDP-bound inactive and GTP-bound active forms, which shift from the inactive to the active state through the action of RALGDS (MIM 601619), which in turn is activated by RAS (see HRAS; MIM 190020) (summary by Feig, 2003 [PubMed 12888294]).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:9841](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9841) · Entrez [10928](https://www.ncbi.nlm.nih.gov/gene/10928) · UniProt [Q15311](https://www.uniprot.org/uniprotkb/Q15311) · Ensembl [ENSG00000017797](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000017797)

## Data

Gene col 303: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 303); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 303, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 303]; `tensor/DDL_lfc|DDL_z.npy` [303]; `embed/gene_vectors.npy` [303]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 303 or target_col == 303). Every well: [[RALBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RALBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
