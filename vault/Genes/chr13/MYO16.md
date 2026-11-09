---
symbol: "MYO16"
type: "gene"
col: 476
ensembl_id: "ENSG00000041515"
name: "myosin XVI"
location: "13q33.3"
module: 75
arm: "+"
pooled_cpm: 4.76
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# MYO16

*myosin XVI* — 13q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.51× (z +20.4, q 0e+00, up in 32 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (LoVo 0.125×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0660×; ⚠ cell-cycle shift, explains ~11% of this change); [[Ranolazine (drug)]] 5 µM in 1 line (A-172 0.0612×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (SW48 0.0717×); [[Mozavaptan (drug)]] 5 µM in 1 line (J82 0.0714×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R9A-AS1]] (+0.82, fdr 7e-06), [[LRRC4C]] (+0.81, fdr 7e-06), [[GALNTL6]] (+0.79, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 476.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.51×** | +20.4 | 0e+00 | 32/37 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.73×** | +16.3 | 0e+00 | 31/39 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.09×** | +12.0 | 1e-30 | 9/11 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.54×** | +10.7 | 1e-24 | 21/27 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.60×** | +10.6 | 4e-24 | 4/6 (A498, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.36×** | +9.9 | 4e-21 | 23/38 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.21×** | +9.1 | 6e-18 | 25/43 (KATO III, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.90×** | +7.4 | 1e-11 | 24/44 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.93×** | +7.3 | 3e-11 | 21/43 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +7.1 | 7e-11 | 18/44 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.80×** | +6.2 | 3e-08 | 7/18 (HEC-1-A, HT-29, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.71×** | +5.7 | 5e-07 | 15/43 (LOX-IMVI, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.3 | 7e-04 | 10/38 (HEC-1-A, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +4.0 | 0.002 | 8/25 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.004 | 8/46 (SW480, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.006 | 9/38 (A549, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.006 | 11/44 (NCI-H1573, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.57×** | +3.7 | 0.007 | 3/28 (HS-578T, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.011 | 11/43 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.026 | 7/43 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (LoVo 0.125×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0660×; ⚠ cell-cycle shift, explains ~11% of this change); [[Ranolazine (drug)]] 5 µM in 1 line (A-172 0.0612×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (SW48 0.0717×); [[Mozavaptan (drug)]] 5 µM in 1 line (J82 0.0714×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 476. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.46 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 22.2× (z +14.5) | [[Ranolazine (drug)]] 5 µM 0.0612× (z -9.2) |
| [[LoVo (line)]] | wt | 14.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.97× (z +17.0) | [[Digitoxin (drug)]] 5 µM 0.125× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 3.76 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.46× (z +9.5) | [[Mozavaptan (drug)]] 5 µM 0.0714× (z -9.2) |
| [[KATO III (line)]] | alt | 4.27 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.82× (z +10.8) | [[Digitoxin (drug)]] 0.5 µM 0.0955× (z -8.7) ⚠ cell-cycle shift, explains ~12% of this change |
| [[NCI-H2347 (line)]] | alt | 3.38 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.79× (z +10.9) | [[Belinostat (drug)]] 0.5 µM 0.0660× (z -11.0) ⚠ cell-cycle shift, explains ~11% of this change |
| [[NCI-H460 (line)]] | wt | 6.03 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +17.2) | — |
| [[A498 (line)]] | wt | 2.41 | 0 | 1 | — | [[Saquinavir (drug)]] 5 µM 0.165× (z -8.7) |
| [[COLO 205 (line)]] | alt | 8.65 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0801× (z -8.6) ⚠ transcription drop; unreliable plate only |
| [[Hs 766T (line)]] | wt | 4.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 3.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.30× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.51 | 0 | 1 | — | [[Capivasertib (drug)]] 0.05 µM 0.0709× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 6.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.88× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 2.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 4.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +13.5) | — |
| [[SW48 (line)]] | wt | 16.7 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0717× (z -9.2) |
| [[SW480 (line)]] | alt | 3.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +10.3) | — |
| [[A-427 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 476), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R9A-AS1]] | +0.82 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.81 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.79 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[NEB]] | +0.78 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.77 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[SLC9C1]] | +0.77 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[MEIOC]] | +0.76 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.75 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[LINC01090]] | +0.75 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[DPP6]] | +0.75 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[LINC01933]] | +0.75 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[GUCY2C-AS1]] | +0.75 | +0.78 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MYO16's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[VENTXP1]] | B | VENTXP1 activity raises MYO16's level | lines that do not express VENTXP1 (12) vs lines expressing it (38) | 1.34× lower at baseline in the lines without VENTXP1 | 0.079 | ⚠ within organs, on part of the lines; also absent: CNTNAP2, SLCO6A1; maybe low, not absent |
| [[ANOS2P]] | B | ANOS2P activity raises MYO16's level | lines that do not express ANOS2P (32) vs lines expressing it (18) | 1.40× lower at baseline in the lines without ANOS2P | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: UTY, EIF1AY, KDM5D |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.869). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.3, 27.9); signed map (32.1, 13.3). **Vector** length 67.1, 10.2% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.5 | +20.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +16.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +12.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +3.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -2.3 | -0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +0.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.6 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | myosin XVI |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q33.3 — chr13:108,596,152-109,208,005 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MYR8, KIAA0865, Myo16b, NYAP3, PPP1R107 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Protein phosphatase 1 regulatory subunits; Myosin heavy chains, class XVI |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6X6](https://www.uniprot.org/uniprotkb/Q9Y6X6) (Unconventional myosin-XVI):

> Myosins are actin-based motor molecules with ATPase activity. Unconventional myosins serve in intracellular movements. Their highly divergent tails are presumed to bind to membranous compartments, which would be moved relative to actin filaments. May be involved in targeting of the catalytic subunit of protein phosphatase 1 during brain development. Activates PI3K and concomitantly recruits the WAVE1 complex to the close vicinity of PI3K and regulates neuronal morphogenesis (By similarity).

**Summary**, from NCBI Gene [23026](https://www.ncbi.nlm.nih.gov/gene/23026):

> This gene encodes an unconventional myosin protein. The encoded protein has been proposed to act as a serine/threonine phosphatase-1 targeting or regulatory subunit. Studies in a rat cell line suggest that this protein may regulate cell cycle progression. A variant within this gene may be associated with susceptibility to schizophrenia and elevated expression of this gene has been observed in the frontal cortex of human schizophrenia patients. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:29822](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29822) · Entrez [23026](https://www.ncbi.nlm.nih.gov/gene/23026) · UniProt [Q9Y6X6](https://www.uniprot.org/uniprotkb/Q9Y6X6) · Ensembl [ENSG00000041515](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000041515)

## Data

Gene col 476: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 476); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 476, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 476]; `tensor/DDL_lfc|DDL_z.npy` [476]; `embed/gene_vectors.npy` [476]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 476 or target_col == 476). Every well: [[MYO16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
