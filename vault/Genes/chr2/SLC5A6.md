---
symbol: "SLC5A6"
type: "gene"
col: 6119
ensembl_id: "ENSG00000138074"
name: "solute carrier family 5 member 6"
location: "2p23.3"
module: 1
arm: "+"
pooled_cpm: 7.39
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 5
n_dd_up_clean: 21
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SLC5A6

*solute carrier family 5 member 6* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.08× (z +13.8, q 8e-41, up in 36 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.633× (z -6.2, q 4e-07, down in 21 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[QTRT1]] (+0.81, fdr 7e-06), [[MCCC2]] (+0.74, fdr 7e-06), [[PIGW]] (+0.73, fdr 1e-05); moves opposite to [[COX6A1]] (-0.63, fdr 3e-05), [[CAST]] (-0.58, fdr 1e-04), [[PJA2]] (-0.58, fdr 1e-04).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6119.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +13.8 | 8e-41 | 36/43 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +10.7 | 3e-24 | 27/43 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.08×** | +9.8 | 2e-20 | 30/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +9.6 | 1e-19 | 11/15 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +9.4 | 9e-19 | 21/36 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.02×** | +9.0 | 2e-17 | 28/45 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +8.0 | 9e-14 | 17/30 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +7.3 | 2e-11 | 8/17 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +6.4 | 1e-08 | 20/41 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +5.6 | 1e-06 | 17/47 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.5 | 2e-06 | 22/42 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.1 | 1e-05 | 13/44 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +5.0 | 2e-05 | 13/33 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +4.8 | 7e-05 | 19/46 (A549, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +4.4 | 3e-04 | 13/46 (LOX-IMVI, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.75×** | +3.9 | 0.003 | 7/39 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.005 | 5/47 (NCI-H460, A498, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.016 | 5/47 (LoVo, NCI-H23, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.63×** | +3.4 | 0.018 | 4/32 (A498, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.62×** | +3.4 | 0.020 | 4/41 (SW1417, NCI-H460, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.020 | 2/42 (NCI-H460, MIA PaCa-2) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6119.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.633×** | -6.2 | 4e-07 | 21/47 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.735×** | -4.1 | 0.010 | 16/41 (KATO III, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.813×** | -3.9 | 0.016 | 14/47 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.758×** | -3.7 | 0.027 | 12/47 (BT-474, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -3.3 | 0.095 | 10/47 (Hs 766T, J82, …) | top dose only |  |
| [[Rifaximin (drug)]] 5 µM |  | **0.776×** | -3.3 | 0.095 | 14/46 (SW 900, CFPAC-1, …) | rises with dose | position effect removed |
| [[Silodosin (drug)]] 5 µM |  | 0.787× | -3.1 | 0.14 | 6/42 (NCI-H2030, MIA PaCa-2, …) | top dose only |  |
| [[Clotrimazole (drug)]] 0.05 µM |  | 0.795× | -3.1 | 0.14 | 11/47 (hTERT-HPNE, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6119. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 6.00 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.109× (z -9.5) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 11.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +12.5) | — |
| [[A498 (line)]] | wt | 8.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 2.88 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.05 µM 0.0652× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 5.66 | 0 | 1 | — | [[Macitentan (drug)]] 5 µM 0.140× (z -9.0) |
| [[KATO III (line)]] | alt | 4.82 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0717× (z -10.0) |
| [[LS 180 (line)]] | wt | 5.78 | 0 | 1 | — | [[Rosiglitazone (drug)]] 5 µM 0.0673× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 5.12 | 0 | 1 | — | [[Ranolazine (drug)]] 0.5 µM 0.0482× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 7.36 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0539× (z -11.4) |
| [[A-172 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6119), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QTRT1]] | +0.81 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[MCCC2]] | +0.74 | +0.69 / +0.64 | both halves | 7e-06 | pathway: Biotin transport and metabolism |
| [[PIGW]] | +0.73 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[DUS3L]] | +0.72 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[SNX5]] | +0.68 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[TMEM147-AS1]] | +0.68 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[PRRC2B]] | +0.66 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[PAXIP1]] | +0.65 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[GTF3C6]] | +0.65 | +0.63 / +0.39 | both halves | 6e-05 |  |
| [[FAIM]] | +0.65 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[DHX37]] | +0.65 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[UTP15]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX6A1]] | -0.63 | -0.58 / -0.43 | both halves | 3e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[CAST]] | -0.58 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[PJA2]] | -0.58 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[NBEAL1]] | -0.57 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[PCSK1N]] | -0.57 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[CARHSP1]] | -0.56 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[YIF1B]] | -0.56 | -0.44 / -0.27 | both halves | 3e-04 |  |
| [[FAM89B]] | -0.55 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[FTL]] | -0.55 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[GAPDH]] | -0.55 | -0.49 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises SLC5A6's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises SLC5A6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PTP4A3]] | B | PTP4A3 activity raises SLC5A6's level | lines that do not express PTP4A3 (7) vs lines expressing it (43) | 1.82× lower at baseline in the lines without PTP4A3 | 0.069 | ⚠ within organs, on part of the lines; also absent: RHOF, RHPN1, JAG2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.562). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-4.6, 6.5); signed map (21.9, -32.1). **Vector** length 74.5, 12.2% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +13.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +10.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.8 | +9.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +3.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +3.4 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -4.1 | -6.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.0 | -4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.0 | -3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 5 member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:27,199,587-27,212,958 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SMVT |
| Gene groups (HGNC) | Solute carrier family 5 |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 7 pathways, smallest: Biotin transport and metabolism; Vitamin B5 (pantothenate) metabolism; Transport of vitamins, nucleosides, and related molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y289](https://www.uniprot.org/uniprotkb/Q9Y289) (Sodium-dependent multivitamin transporter):

> Sodium-dependent multivitamin transporter that mediates the electrogenic transport of pantothenate, biotin, lipoate and iodide. Functions as a Na(+)-coupled substrate symporter where the stoichiometry of Na(+):substrate is 2:1, creating an electrochemical Na(+) gradient used as driving force for substrate uptake. Required for biotin and pantothenate uptake in the intestine across the brush border membrane. Plays a role in the maintenance of intestinal mucosa integrity, by providing the gut …

**Summary**, from NCBI Gene [8884](https://www.ncbi.nlm.nih.gov/gene/8884):

> Enables biotin transmembrane transporter activity; iodide transmembrane transporter activity; and pantothenate transmembrane transporter activity. Involved in iodide transmembrane transport; transport across blood-brain barrier; and vitamin transmembrane transport. Located in apical plasma membrane. Implicated in vitamin metabolic disorder. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11041](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11041) · Entrez [8884](https://www.ncbi.nlm.nih.gov/gene/8884) · UniProt [Q9Y289](https://www.uniprot.org/uniprotkb/Q9Y289) · Ensembl [ENSG00000138074](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138074)

## Data

Gene col 6119: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6119); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6119, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6119]; `tensor/DDL_lfc|DDL_z.npy` [6119]; `embed/gene_vectors.npy` [6119]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6119 or target_col == 6119). Every well: [[SLC5A6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC5A6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
