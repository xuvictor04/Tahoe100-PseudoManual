---
symbol: "SEC14L4"
type: "gene"
col: 5453
ensembl_id: "ENSG00000133488"
name: "SEC14 like lipid binding 4"
location: "22q12.2"
module: 128
arm: "+"
pooled_cpm: 2.83
n_lines_expressing: 21
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# SEC14L4

*SEC14 like lipid binding 4* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.04× (z +12.0, q 4e-30, up in 2 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.72× (z +5.3, q 2e-05, up in 9 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.463× (z -5.3, q 7e-05, down in 16 of 18 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BOLA3-DT]] (+0.60, fdr 4e-05), [[TBX1]] (+0.57, fdr 1e-05), [[BARX1]] (+0.56, fdr 9e-05); moves opposite to [[PCNT]] (-0.38, fdr 4e-04).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FBXO17]] → it (grade B ⚠); 3 go from it, the strongest it → [[BOLA3-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5453.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.04×** | +12.0 | 4e-30 | 2/6 (NCI-H2347, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.99×** | +7.6 | 1e-11 | 4/9 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.75×** | +6.5 | 2e-08 | 4/8 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +5.3 | 2e-05 | 9/17 (HOP62, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.13×** | +5.2 | 2e-05 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.85×** | +5.2 | 2e-05 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.1 | 0.004 | 0/15 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.006 | 8/18 (RKO, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +3.7 | 0.012 | 1/12 (NCI-H2347) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +3.7 | 0.013 | 10/16 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.10×** | +3.7 | 0.013 | 3/13 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.6 | 0.014 | 1/9 (NCI-H23) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.04×** | +3.5 | 0.018 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.4 | 0.032 | 2/12 (A549, RKO) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.56×** | +3.1 | 0.076 | 5/17 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.56×** | +3.1 | 0.076 | 1/12 (SW1417) | inconsistent across doses | low cells (technical?) |
| [[Saquinavir (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.100 | 1/14 (SW480) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.82×** | +3.0 | 0.100 | 1/13 (MIA PaCa-2) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5453.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.463×** | -5.3 | 7e-05 | 16/18 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.473×** | -5.1 | 8e-05 | 13/18 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.602×** | -3.5 | 0.094 | 9/18 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | 0.605× | -3.3 | 0.11 | 13/18 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.619× | -3.3 | 0.11 | 5/18 (A-427, NCI-H460, …) | inconsistent across doses |  |
| [[Orlistat (drug)]] 5 µM |  | 0.631× | -3.0 | 0.23 | 3/18 (HOP62, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5453. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.98 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -13.8) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0701× (z -13.5) |
| [[A549 (line)]] | wt | 12.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0314× (z -24.0) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0612× (z -13.7) |
| [[SW480 (line)]] | alt | 11.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -12.9) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 18.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.111× (z -11.1) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 3.12 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0633× (z -9.0) ⚠ cell-cycle shift, explains ~63% of this change |
| [[HOP62 (line)]] | alt | 2.74 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -10.5) ⚠ cell-cycle shift, explains ~63% of this change |
| [[MIA PaCa-2 (line)]] | alt | 5.12 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.1000× (z -8.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.258 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.289 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.248 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.976 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.363 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.278 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.487 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.338 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.344 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.228 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.251 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.240 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.270 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.298 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5453), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BOLA3-DT]] | +0.60 | +0.58 / +0.40 | both halves | 4e-05 | **novel candidate** |
| [[TBX1]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[BARX1]] | +0.56 | +0.53 / +0.37 | both halves | 9e-05 | **novel candidate** |
| [[LINC00173]] | +0.56 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[CFAP298-TCP10L]] | +0.53 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[PTPN20]] | +0.53 | +0.49 / +0.38 | both halves | 7e-05 |  |
| [[LAMC3]] | +0.53 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[HEYL]] | +0.51 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[DIO3OS]] | +0.51 | +0.46 / +0.35 | both halves | 1e-04 |  |
| [[TMEM74B]] | +0.51 | +0.52 / +0.30 | both halves | 2e-04 |  |
| [[ACBD4]] | +0.50 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[F10]] | +0.50 | +0.50 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNT]] | -0.38 | -0.26 / -0.51 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO17]] | B | FBXO17 activity raises SEC14L4's level | lines that do not express FBXO17 (18) vs lines expressing it (32) | 1.57× lower at baseline in the lines without FBXO17 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, MRC2, MIR130AHG |
| [[PRRX2]] | C | PRRX2 activity raises SEC14L4's level | lines that do not express PRRX2 (24) vs lines expressing it (26) | 1.79× lower at baseline in the lines without PRRX2 | 0.094 | ⚠ within organs, on part of the lines; also absent: PTCHD1, CYP27C1, STOX2; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BOLA3-DT]] | B | SEC14L4 activity raises BOLA3-DT's level | lines that do not express SEC14L4 (29) vs lines expressing it (21) | 1.44× lower at baseline in the lines without SEC14L4 | 0.060 | ⚠ within organs, on part of the lines; also absent: WT1-AS, ACP7, PLTP |
| [[JAK3]] | B | SEC14L4 activity raises JAK3's level | lines that do not express SEC14L4 (29) vs lines expressing it (21) | 2.18× lower at baseline in the lines without SEC14L4 | 0.068 | ⚠ within organs, on part of the lines; also absent: WT1-AS, ACP7, PLTP |
| [[FBXO17]] | B | SEC14L4 activity raises FBXO17's level | lines that do not express SEC14L4 (29) vs lines expressing it (21) | 2.22× lower at baseline in the lines without SEC14L4 | 0.097 | ⚠ within organs, on part of the lines; also absent: WT1-AS, ACP7, PLTP |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.491). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.0, 40.3); signed map (22.3, 25.4). **Vector** length 38.5, 8.81% of its response variance represented; |z| ≥ 3 in 419 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.8 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +6.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.8 | +0.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.7 | +2.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -5.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.0 | -3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.2 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.8 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -1.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | SEC14 like lipid binding 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:30,488,902-30,505,711 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TAP3, dJ130H16.5 |
| Gene groups (HGNC) | SEC14 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UDX3](https://www.uniprot.org/uniprotkb/Q9UDX3) (SEC14-like protein 4):

> Probable hydrophobic ligand-binding protein; may play a role in the transport of hydrophobic ligands like tocopherol, squalene and phospholipids.

**Summary**, from NCBI Gene [284904](https://www.ncbi.nlm.nih.gov/gene/284904):

> The protein encoded by this gene is highly similar to the protein encoded by the Saccharomyces cerevisiae SEC14 gene. The SEC14 protein is a phophatidylinositol transfer protein that is essential for biogenesis of Golgi-derived transport vesicles, and thus is required for the export of yeast secretory proteins from the Golgi complex. The specific function of this protein has not yet been determined. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2009]

**Accessions** — [HGNC:20627](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20627) · Entrez [284904](https://www.ncbi.nlm.nih.gov/gene/284904) · UniProt [Q9UDX3](https://www.uniprot.org/uniprotkb/Q9UDX3) · Ensembl [ENSG00000133488](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133488)

## Data

Gene col 5453: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5453); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5453, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5453]; `tensor/DDL_lfc|DDL_z.npy` [5453]; `embed/gene_vectors.npy` [5453]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5453 or target_col == 5453). Every well: [[SEC14L4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC14L4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
