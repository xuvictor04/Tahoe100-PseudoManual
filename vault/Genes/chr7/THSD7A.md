---
symbol: "THSD7A"
type: "gene"
col: 68
ensembl_id: "ENSG00000005108"
name: "thrombospondin type 1 domain containing 7A"
location: "7p21.3"
module: 9
arm: "+"
pooled_cpm: 29.86
n_lines_expressing: 24
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 27
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# THSD7A

*thrombospondin type 1 domain containing 7A* — 7p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.00× (z +20.8, q 0e+00, up in 15 of 22 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SHP-77 0.223×, NCI-H460 0.240×); [[Panobinostat (drug)]] 5 µM in 2 lines (SHP-77 0.190×, A-427 0.227×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 2 lines (A-427 0.218×, SHP-77 0.217×; ⚠ cell-cycle shift, explains ~95% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0902×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SHP-77 0.177×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHA5-AS1]] (+0.69, fdr 7e-06), [[MIR99AHG]] (+0.66, fdr 7e-06), [[EPHA5]] (+0.64, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TBX18]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 68.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.00×** | +20.8 | 0e+00 | 15/22 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.86×** | +14.3 | 4e-44 | 18/21 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.20×** | +12.3 | 1e-32 | 11/21 (NCI-H1573, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +8.7 | 4e-16 | 6/18 (SW 900, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +8.6 | 1e-15 | 7/17 (HEC-1-A, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.17×** | +7.9 | 3e-13 | 11/21 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.98×** | +7.2 | 4e-11 | 10/21 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.94×** | +7.0 | 1e-10 | 14/21 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +6.8 | 9e-10 | 9/22 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.72×** | +5.7 | 6e-07 | 16/21 (HEC-1-A, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.5 | 2e-06 | 3/22 (NCI-H1792, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +5.2 | 1e-05 | 7/21 (SK-MEL-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +4.9 | 4e-05 | 10/21 (NCI-H2347, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.61×** | +4.9 | 5e-05 | 15/21 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.57×** | +4.6 | 1e-04 | 10/21 (NCI-H1573, CHP-212, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +4.4 | 3e-04 | 10/21 (A-172, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.47×** | +4.1 | 0.001 | 9/21 (A-427, PANC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.45×** | +3.9 | 0.002 | 7/21 (SHP-77, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 68.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SHP-77 0.223×, NCI-H460 0.240×); [[Panobinostat (drug)]] 5 µM in 2 lines (SHP-77 0.190×, A-427 0.227×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 2 lines (A-427 0.218×, SHP-77 0.217×; ⚠ cell-cycle shift, explains ~95% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0902×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SHP-77 0.177×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | 0.748× | -3.1 | 0.67 | 5/21 (A-427, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Asciminib (drug)]] 0.05 µM |  | 0.751× | -3.0 | 0.67 | 7/21 (NCI-H1792, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 68. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 148 | 0 | 9 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0851× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -15.1) |
| [[A-427 (line)]] | wt | 181 | 0 | 8 (6 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0441× (z -12.4) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -9.8) |
| [[A-172 (line)]] | wt | 11.7 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.5× (z +17.8) | — |
| [[NCI-H1573 (line)]] | alt | 28.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +17.2) | — |
| [[NCI-H460 (line)]] | wt | 80.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0902× (z -16.5) |
| [[BT-474 (line)]] | alt | 7.83 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 102× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 8.36 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 45.7× (z +14.7) | — |
| [[HOP62 (line)]] | alt | 9.90 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.68× (z +11.7) | — |
| [[KATO III (line)]] | alt | 9.82 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.33× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 43.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +14.8) | — |
| [[HEC-1-A (line)]] | alt | 96.1 | 1 (1 ⚠) | 0 | [[Trametinib (drug)]] 5 µM 4.66× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2030 (line)]] | alt | 54.9 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.97× (z +9.9) ⚠ position not correctable | — |
| [[SNU-423 (line)]] | alt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.04× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0886× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.37 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.08 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.94 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.31 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.03 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 84.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.14 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.25 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.07 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.11 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.53 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.09 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.31 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.29 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 68), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA5-AS1]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[MIR99AHG]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[EPHA5]] | +0.64 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[ID4]] | +0.63 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[PDE1A]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[HECW2]] | +0.62 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[SEMA3E]] | +0.61 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[ZSCAN31]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[FGF14]] | +0.61 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[LRP1B]] | +0.61 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[NKAIN2]] | +0.61 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[LINC02211]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBX18]] | B | TBX18 activity raises THSD7A's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 2.57× lower at baseline in the lines without TBX18 | 0.093 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251 |
| [[BAGE2]] | C | BAGE2 activity raises THSD7A's level | lines that do not express BAGE2 (36) vs lines expressing it (14) | 1.95× lower at baseline in the lines without BAGE2 | 0.044 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TPTE, ENSG00000260289, LINC01029; co-absent with the target |
| [[LRMDA]] | C | LRMDA activity raises THSD7A's level | lines that do not express LRMDA (21) vs lines expressing it (29) | 2.41× lower at baseline in the lines without LRMDA | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, CCL28, SMIM10; co-absent with the target |
| [[LINC01029]] | C | LINC01029 activity raises THSD7A's level | lines that do not express LINC01029 (42) vs lines expressing it (8) | 2.98× lower at baseline in the lines without LINC01029 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, LINC00879, OVAAL; co-absent with the target |
| [[NAALADL2-AS2]] | C | NAALADL2-AS2 activity raises THSD7A's level | lines that do not express NAALADL2-AS2 (36) vs lines expressing it (14) | 3.20× lower at baseline in the lines without NAALADL2-AS2 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RNF17, ENSG00000287598, SSX1; co-absent with the target |
| [[BMP5]] | C | BMP5 activity raises THSD7A's level | lines that do not express BMP5 (38) vs lines expressing it (12) | 2.77× lower at baseline in the lines without BMP5 | 0.098 | ⚠ within organs, on part of the lines; also absent: LINC01035, CPLX2, SCG3; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.4, 32.6); signed map (40.1, 34.7). **Vector** length 85.5, 25.9% of its response variance represented; |z| ≥ 3 in 719 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.1 | +12.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.5 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.5 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +20.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +5.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.0 | +4.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | -2.8 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.0 | -1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -1.6 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.9 | -3.0 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | thrombospondin type 1 domain containing 7A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.3 — chr7:11,370,365-11,832,198 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0960 |
| Reactome | 6 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPZ6](https://www.uniprot.org/uniprotkb/Q9UPZ6) (Thrombospondin type-1 domain-containing protein 7A):

> [Thrombospondin type-1 domain-containing protein 7A]: Plays a role in actin cytoskeleton rearrangement.; [Thrombospondin type-1 domain-containing protein 7A, soluble form]: The soluble form promotes endothelial cell migration and filopodia formation during sprouting angiogenesis via a FAK-dependent mechanism.

**Summary**, from NCBI Gene [221981](https://www.ncbi.nlm.nih.gov/gene/221981):

> The protein encoded by this gene is found almost exclusively in endothelial cells from placenta and umbilical cord. The encoded protein appears to interact with alpha(V)beta(3) integrin and paxillin to inhibit endothelial cell migration and tube formation. This protein may be involved in cytoskeletal organization. Variations in this gene may be associated with low bone mineral density in osteoporosis. [provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:22207](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22207) · Entrez [221981](https://www.ncbi.nlm.nih.gov/gene/221981) · UniProt [Q9UPZ6](https://www.uniprot.org/uniprotkb/Q9UPZ6) · Ensembl [ENSG00000005108](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005108)

## Data

Gene col 68: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 68); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 68, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 68]; `tensor/DDL_lfc|DDL_z.npy` [68]; `embed/gene_vectors.npy` [68]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 68 or target_col == 68). Every well: [[THSD7A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THSD7A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
