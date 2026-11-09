---
symbol: "SPACDR"
type: "gene"
col: 11759
ensembl_id: "ENSG00000185955"
name: "sperm acrosome developmental regulator"
location: "7q22.1"
module: 38
arm: "+"
pooled_cpm: 8.27
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 22
n_dd_up_clean: 10
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# SPACDR

*sperm acrosome developmental regulator* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.16× (z +10.4, q 1e-22, up in 32 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.471× (z -7.2, q 4e-10, down in 31 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHKG1]] (+0.74, fdr 7e-06), [[TNXB]] (+0.69, fdr 7e-06), [[NOXRED1]] (+0.68, fdr 1e-05); moves opposite to [[OCRL]] (-0.63, fdr 1e-05), [[VMA21]] (-0.62, fdr 1e-05), [[PPIL1]] (-0.62, fdr 9e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11759.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +10.4 | 1e-22 | 32/41 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +6.5 | 2e-08 | 23/41 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.82×** | +5.7 | 2e-06 | 23/39 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +4.3 | 0.003 | 18/40 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.2 | 0.003 | 14/35 (MIA PaCa-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.009 | 18/44 (HOP62, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +3.9 | 0.009 | 10/46 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.71×** | +3.7 | 0.017 | 11/37 (NCI-H23, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **1.39×** | +3.2 | 0.094 | 15/46 (PANC-1, NCI-H1792, …) | all doses, flat |  |
| [[Vilanterol (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.098 | 6/46 (Panc 03.27, SK-MEL-2, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.098 | 5/45 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11759.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.471×** | -7.2 | 4e-10 | 31/45 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.503×** | -6.6 | 2e-08 | 30/44 (PANC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.510×** | -6.4 | 2e-08 | 26/45 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.502×** | -6.3 | 4e-08 | 24/45 (BT-474, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.549×** | -5.7 | 1e-06 | 24/32 (MIA PaCa-2, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.550×** | -5.7 | 1e-06 | 23/45 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.551×** | -5.7 | 1e-06 | 22/41 (NCI-H1573, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.574×** | -5.3 | 8e-06 | 27/47 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.577×** | -5.3 | 9e-06 | 25/45 (SNU-423, H4, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.584×** | -4.9 | 4e-05 | 22/43 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.602×** | -4.5 | 4e-04 | 20/38 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.625×** | -4.4 | 4e-04 | 20/41 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.637×** | -4.3 | 8e-04 | 22/46 (SNU-423, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.641×** | -4.2 | 9e-04 | 23/46 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.754×** | -3.8 | 0.006 | 21/47 (MIA PaCa-2, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.677×** | -3.6 | 0.013 | 15/42 (A-172, HS-578T, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.702×** | -3.4 | 0.025 | 15/46 (NCI-H1573, NCI-H23, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.782×** | -3.3 | 0.030 | 15/47 (RPMI-7951, SNU-423, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11759. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 17.0 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0540× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.108× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 16.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.128× (z -10.8) |
| [[A498 (line)]] | wt | 9.11 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 15.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A549 (line)]] | wt | 6.01 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.56× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 5.65 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0521× (z -8.5) |
| [[C32 (line)]] | wt | 23.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +8.6) | — |
| [[J82 (line)]] | alt | 5.01 | 0 | 1 | — | [[Ixazomib (drug)]] 0.05 µM 0.0931× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 8.20 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0422× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 6.18 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0880× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 6.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 8.57 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0562× (z -11.8) |
| [[PANC-1 (line)]] | alt | 6.08 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11759), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHKG1]] | +0.74 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[TNXB]] | +0.69 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[NOXRED1]] | +0.68 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[ISY1-RAB43]] | +0.68 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[DHDH]] | +0.67 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[CCDC65]] | +0.67 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[ATP2A1]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[TINCR]] | +0.66 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[MARK4]] | +0.65 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[LINC00672]] | +0.65 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[TMEM38A]] | +0.65 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[BNIPL]] | +0.63 | +0.51 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OCRL]] | -0.63 | -0.49 / -0.70 | both halves | 1e-05 |  |
| [[VMA21]] | -0.62 | -0.54 / -0.67 | both halves | 1e-05 |  |
| [[PPIL1]] | -0.62 | -0.57 / -0.62 | both halves | 9e-06 |  |
| [[ATIC]] | -0.61 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[EFR3A]] | -0.60 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[GFM1]] | -0.60 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[FARSB]] | -0.60 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[ICMT]] | -0.59 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[IDH3A]] | -0.59 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[MBTPS2]] | -0.58 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[AKAP11]] | -0.57 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[PRPS1]] | -0.57 | -0.43 / -0.68 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SPACDR's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[C4orf47]] | C | C4orf47 activity raises SPACDR's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 2.06× lower at baseline in the lines without C4orf47 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.6, -21.9); signed map (11.0, 9.7). **Vector** length 99.4, 22.1% of its response variance represented; |z| ≥ 3 in 1,031 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +10.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.2 | +5.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.9 | +2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +6.5 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +1.4 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -5.6 | -4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.6 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -6.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -7.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -3.7 | -2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -4.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | sperm acrosome developmental regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,456,620-100,464,260 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IMAGE:4839025; previously C7orf61 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZ16](https://www.uniprot.org/uniprotkb/Q8IZ16) (Sperm acrosome developmental regulator):

> May play a role in acrosome formation and nucleus shaping during spermiogenesis.

**Summary**, from NCBI Gene [402573](https://www.ncbi.nlm.nih.gov/gene/402573):

> Involved in spermatid development. Located in acrosomal vesicle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22135](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22135) · Entrez [402573](https://www.ncbi.nlm.nih.gov/gene/402573) · UniProt [Q8IZ16](https://www.uniprot.org/uniprotkb/Q8IZ16) · Ensembl [ENSG00000185955](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185955)

## Data

Gene col 11759: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11759); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11759, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11759]; `tensor/DDL_lfc|DDL_z.npy` [11759]; `embed/gene_vectors.npy` [11759]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11759 or target_col == 11759). Every well: [[SPACDR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPACDR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
