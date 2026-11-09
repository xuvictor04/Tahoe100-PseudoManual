---
symbol: "DOK3"
type: "gene"
col: 7064
ensembl_id: "ENSG00000146094"
name: "docking protein 3"
location: "5q35.3"
module: 47
arm: "+"
pooled_cpm: 9.86
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# DOK3

*docking protein 3* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 1.74× (z +5.2, q 1e-04, up in 22 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.295× (z -11.4, q 2e-27, down in 31 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.312× (z -11.0, q 7e-26, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC23]] (+0.73, fdr 7e-06), [[SMIM41]] (+0.69, fdr 7e-06), [[PYGM]] (+0.68, fdr 7e-06); moves opposite to [[BBS7]] (-0.55, fdr 2e-05), [[P2RX4]] (-0.54, fdr 3e-05), [[HACD2]] (-0.53, fdr 2e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PPP1R16A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7064.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **1.74×** | +5.2 | 1e-04 | 22/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.46×** | +5.0 | 2e-04 | 20/42 (PANC-1, HOP62, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.62×** | +4.4 | 0.002 | 15/47 (A549, NCI-H23, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.62×** | +4.2 | 0.003 | 8/23 (NCI-H460, NCI-H2347, …) | inconsistent across doses | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.55×** | +4.1 | 0.005 | 17/47 (NCI-H460, SNU-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.54×** | +4.0 | 0.005 | 19/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Roxadustat (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.096 | 18/45 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.88× | +3.1 | 0.12 | 11/40 (C-33 A, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Tetracycline (hydrochloride) (drug)]] 0.05 µM |  | 1.43× | +3.1 | 0.12 | 6/45 (A-427, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7064.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.295×** | -11.4 | 2e-27 | 31/39 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.312×** | -11.0 | 7e-26 | 37/47 (hTERT-HPNE, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.319×** | -10.7 | 2e-24 | 38/47 (C-33 A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.388×** | -9.0 | 4e-17 | 37/44 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.461×** | -7.1 | 2e-10 | 26/45 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.481×** | -6.7 | 2e-09 | 25/39 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.492×** | -6.5 | 5e-09 | 26/45 (J82, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.646×** | -5.9 | 3e-07 | 25/44 (C32, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.538×** | -5.7 | 6e-07 | 27/47 (SNU-423, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.573×** | -5.3 | 7e-06 | 21/46 (SW 900, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.668×** | -3.7 | 0.011 | 17/43 (HEC-1-A, SW 900, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.670×** | -3.5 | 0.019 | 10/39 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.726×** | -3.1 | 0.097 | 17/43 (C32, SW 900, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.720× | -3.0 | 0.10 | 18/45 (HEC-1-A, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7064. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 57.6 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0725× (z -19.4) |
| [[SNU-423 (line)]] | alt | 19.8 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0788× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 29.2 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0711× (z -13.0) |
| [[C-33 A (line)]] | alt | 34.8 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0201× (z -16.4) |
| [[J82 (line)]] | alt | 13.8 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0871× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 4.70 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0333× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 3.68 | 0 | 3 (1 ⚠) | — | [[Flutamide (drug)]] 0.5 µM 0.0628× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 10.3 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0645× (z -11.7) |
| [[A-172 (line)]] | wt | 14.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0284× (z -14.5) |
| [[HEC-1-A (line)]] | alt | 14.8 | 0 | 2 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0633× (z -15.0) |
| [[LOX-IMVI (line)]] | wt | 9.21 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0407× (z -15.5) |
| [[NCI-H2030 (line)]] | alt | 9.21 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0448× (z -13.8) |
| [[RPMI-7951 (line)]] | alt | 8.26 | 0 | 2 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0638× (z -9.1) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.0658× (z -8.8) |
| [[SW 900 (line)]] | alt | 13.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0756× (z -11.5) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.0957× (z -10.0) |
| [[A-427 (line)]] | wt | 9.16 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0964× (z -9.4) |
| [[H4 (line)]] | wt | 17.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0473× (z -11.7) |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.111× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 8.73 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0379× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0688× (z -12.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 4.87 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.153× (z -8.6) |
| [[A498 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7064), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC23]] | +0.73 | +0.71 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[SMIM41]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[PYGM]] | +0.68 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[ATP2A1]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[RFPL3S]] | +0.65 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[NPAS1]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[FERMT3]] | +0.65 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[CPT1C]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[GDF1]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[MSANTD1]] | +0.61 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[VWCE]] | +0.61 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.61 | +0.64 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBS7]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[P2RX4]] | -0.54 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[HACD2]] | -0.53 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[VPS36]] | -0.52 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[EFR3A]] | -0.52 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[PTAR1]] | -0.52 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[PON2]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers DOK3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[KDM2B-DT]] | B | KDM2B-DT activity raises DOK3's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 2.26× lower at baseline in the lines without KDM2B-DT | 0.094 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R16A]] | C | DOK3's natural level strengthens PPP1R16A's drug response | DOK3's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.25; direction not clear | 0.063 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.0, -18.5); signed map (15.2, 13.7). **Vector** length 102, 23.8% of its response variance represented; |z| ≥ 3 in 1,211 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | -0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.7 | +3.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.6 | +5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | -1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +2.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.3 | -9.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.9 | -6.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.7 | -11.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.5 | -10.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.4 | -11.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.9 | -3.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -3.0 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -1.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | docking protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:177,501,904-177,511,274 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22570 |
| Gene groups (HGNC) | Docking protein family |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L591](https://www.uniprot.org/uniprotkb/Q7L591) (Docking protein 3):

> DOK proteins are enzymatically inert adaptor or scaffolding proteins. They provide a docking platform for the assembly of multimolecular signaling complexes. DOK3 is a negative regulator of JNK signaling in B-cells through interaction with INPP5D/SHIP1. May modulate ABL1 function (By similarity).

**Summary**, from NCBI Gene [79930](https://www.ncbi.nlm.nih.gov/gene/79930):

> Predicted to enable signaling adaptor activity. Predicted to be involved in Ras protein signal transduction. Located in plasma membrane. Implicated in colorectal adenocarcinoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24583](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24583) · Entrez [79930](https://www.ncbi.nlm.nih.gov/gene/79930) · UniProt [Q7L591](https://www.uniprot.org/uniprotkb/Q7L591) · Ensembl [ENSG00000146094](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146094)

## Data

Gene col 7064: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7064); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7064, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7064]; `tensor/DDL_lfc|DDL_z.npy` [7064]; `embed/gene_vectors.npy` [7064]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7064 or target_col == 7064). Every well: [[DOK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
