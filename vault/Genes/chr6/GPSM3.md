---
symbol: "GPSM3"
type: "gene"
col: 13123
ensembl_id: "ENSG00000213654"
name: "G protein signaling modulator 3"
location: "6p21.32"
module: 196
arm: "+"
pooled_cpm: 3.53
n_lines_expressing: 31
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/196"]
generated_by: "tahoemap"
---

# GPSM3

*G protein signaling modulator 3* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.86× (z +10.6, q 2e-23, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +5.8, q 1e-06, up in 4 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.501× (z -4.9, q 7e-04, down in 16 of 24 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCAT1]] (+0.60, fdr 3e-05), [[FES]] (+0.59, fdr 1e-05), [[IL19]] (+0.55, fdr 3e-05); moves opposite to [[SFXN4]] (-0.39, fdr 8e-05).
> It is in [[Module 196]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[S100A3]] → it (grade B ⚠); 3 go from it, the strongest it → [[IL19]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13123.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.86×** | +10.6 | 2e-23 | 3/4 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.58×** | +8.9 | 2e-16 | 8/10 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +5.8 | 1e-06 | 4/19 (PANC-1, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.29×** | +5.7 | 1e-06 | 4/9 (SK-MEL-2, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +5.7 | 1e-06 | 4/6 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.73×** | +5.3 | 9e-06 | 2/26 (SNU-423, SW480) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.63×** | +3.4 | 0.056 | 3/16 (SNU-423, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.3 | 0.061 | 1/14 (NCI-H2030) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.2 | 0.078 | 4/16 (HOP62, NCI-H460, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.02×** | +3.2 | 0.078 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.35×** | +3.1 | 0.100 | 0/5 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13123.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.501×** | -4.9 | 7e-04 | 16/24 (SW480, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.551×** | -4.2 | 0.007 | 7/25 (LOX-IMVI, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.557×** | -4.1 | 0.007 | 11/24 (CFPAC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.533×** | -4.0 | 0.009 | 15/25 (H4, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.589×** | -3.7 | 0.021 | 9/25 (SNU-423, SW1417, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.592×** | -3.7 | 0.021 | 16/25 (SW480, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.600×** | -3.6 | 0.026 | 15/26 (SNU-423, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.399×** | -3.4 | 0.052 | 8/24 (NCI-H2030, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.613×** | -3.3 | 0.068 | 14/24 (J82, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.613×** | -3.2 | 0.068 | 6/26 (SW480, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13123. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 20.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -9.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.180× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 8.31 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -11.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.120× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 2.99 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.7× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 39.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 7.30 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0863× (z -8.5) ⚠ toxic |
| [[SW480 (line)]] | alt | 3.53 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -8.6) |
| [[A-172 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.673 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.370 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.566 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.965 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.639 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.857 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.369 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.889 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.242 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.354 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.741 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13123), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAT1]] | +0.60 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[FES]] | +0.59 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[IL19]] | +0.55 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[LAPTM5]] | +0.54 | +0.54 / +0.44 | both halves | 3e-05 | STRING 405 |
| [[MILR1]] | +0.53 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[LIMD2]] | +0.53 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[CACNA2D4]] | +0.52 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[IGF2BP2-AS1]] | +0.52 | +0.35 / +0.61 | both halves | 1e-04 |  |
| [[RGL2]] | +0.51 | +0.39 / +0.67 | both halves | 6e-05 |  |
| [[ETV1]] | +0.51 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[MEI1]] | +0.50 | +0.36 / +0.39 | both halves | 9e-05 |  |
| [[PAEP]] | +0.49 | +0.46 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFXN4]] | -0.39 | -0.37 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100A3]] | B | S100A3 activity weakens GPSM3's drug response | lines that do not express S100A3 (7) vs lines expressing it (19) | the lines without S100A3 respond 1.23× as strongly (z diff -0.48); rises at some drug-doses, falls at others (47% from rises): Dinaciclib 5 µM: 1.97x vs 0.80x (z diff -5.0); Dinaciclib 0.5 µM: 2.69x vs 2.35x (z diff -3.3); Panobinostat 0.5 µM: 0.37x vs 0.50x (z diff -2.4) | 0.085 | ⚠ within organs, on part of the lines; also absent: S100A4; maybe low, not absent; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |
| [[FKBP9P1-1]] | C | FKBP9P1-1 activity raises GPSM3's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 1.76× lower at baseline in the lines without FKBP9P1-1 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL19]] | B | GPSM3 activity raises IL19's level | lines that do not express GPSM3 (19) vs lines expressing it (31) | 1.71× lower at baseline in the lines without GPSM3 | 0.027 | ⚠ within organs, on part of the lines; also absent: NAV1, CDK15, PAMR1 |
| [[DIO3OS]] | B | GPSM3 activity raises DIO3OS's level | lines that do not express GPSM3 (19) vs lines expressing it (31) | 1.51× lower at baseline in the lines without GPSM3 | 0.040 | ⚠ within organs, on part of the lines; also absent: NAV1, CDK15, PAMR1 |
| [[CACNA2D4]] | B | GPSM3 activity raises CACNA2D4's level | lines that do not express GPSM3 (19) vs lines expressing it (31) | 1.71× lower at baseline in the lines without GPSM3 | 0.043 | ⚠ within organs, on part of the lines; also absent: NAV1, CDK15, PAMR1 |

## Where it sits

- **Module**: [[Module 196]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.467). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (53.4, -0.1); signed map (10.1, 53.8). **Vector** length 36.7, 6.02% of its response variance represented; |z| ≥ 3 in 568 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +5.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | -0.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.9 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.8 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +2.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.0 | -3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -1.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.1 | -2.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | G protein signaling modulator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:32,190,766-32,195,523 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NG1, G18, G18.1a, G18.1b, G18.2, AGS4; previously C6orf9 |
| Reactome | 3 pathways, smallest: G alpha (i) signalling events; GPCR downstream signalling; Signaling by GPCR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4H4](https://www.uniprot.org/uniprotkb/Q9Y4H4) (G protein-signaling modulator 3):

> Interacts with subunit of G(i) alpha proteins and regulates the activation of G(i) alpha proteins.

**Summary**, from NCBI Gene [63940](https://www.ncbi.nlm.nih.gov/gene/63940):

> Predicted to enable GTPase regulator activity. Predicted to be involved in positive regulation of inflammatory response. Predicted to act upstream of or within positive regulation of cytokine production involved in inflammatory response and positive regulation of leukocyte chemotaxis. Predicted to be located in cytoplasm and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13945](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13945) · Entrez [63940](https://www.ncbi.nlm.nih.gov/gene/63940) · UniProt [Q9Y4H4](https://www.uniprot.org/uniprotkb/Q9Y4H4) · Ensembl [ENSG00000213654](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213654)

## Data

Gene col 13123: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13123); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13123, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13123]; `tensor/DDL_lfc|DDL_z.npy` [13123]; `embed/gene_vectors.npy` [13123]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13123 or target_col == 13123). Every well: [[GPSM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPSM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
