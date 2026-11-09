---
symbol: "C7orf57"
type: "gene"
col: 9000
ensembl_id: "ENSG00000164746"
name: "chromosome 7 open reading frame 57"
location: "7p12.3"
module: 154
arm: "+"
pooled_cpm: 2.41
n_lines_expressing: 32
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 5
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# C7orf57

*chromosome 7 open reading frame 57* — 7p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 16.4× (z +20.4, q 0e+00, up in 25 of 26 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Clobetasol propionate (drug)]] 5 µM in 1 line (A498 0.0301×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3GL3]] (+0.69, fdr 1e-05), [[CALB2]] (+0.66, fdr 8e-06), [[CIB1]] (+0.63, fdr 2e-05); moves opposite to [[IL1R1]] (-0.58, fdr 1e-05), [[SUCLA2]] (-0.55, fdr 2e-05), [[STXBP5]] (-0.55, fdr 5e-05).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 5 go from it, the strongest it → [[PI4K2A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9000.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **16.4×** | +20.4 | 0e+00 | 25/26 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **13.4×** | +18.9 | 0e+00 | 24/25 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **12.5×** | +18.4 | 0e+00 | 25/26 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.70×** | +11.2 | 4e-27 | 24/26 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.87×** | +10.8 | 4e-25 | 19/22 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.96×** | +9.6 | 7e-20 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.20×** | +8.4 | 2e-15 | 2/11 (HOP62, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.27×** | +8.0 | 1e-13 | 2/8 (PANC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **6.14×** | +6.9 | 3e-10 | 18/24 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.55×** | +6.8 | 7e-10 | 13/17 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +5.9 | 2e-07 | 9/20 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.18×** | +5.6 | 8e-07 | 13/26 (J82, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +5.5 | 2e-06 | 5/22 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +5.4 | 3e-06 | 3/12 (A-172, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.93×** | +4.8 | 7e-05 | 10/24 (SW480, A-172, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.50×** | +4.7 | 8e-05 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +4.7 | 8e-05 | 7/15 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +4.2 | 6e-04 | 10/26 (SW480, NCI-H460, …) | top dose only |  |
| [[Vilanterol (drug)]] 0.05 µM |  | **1.66×** | +3.7 | 0.007 | 2/22 (Hs 766T, Panc 03.27) | inconsistent across doses | position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Clobetasol propionate (drug)]] 5 µM in 1 line (A498 0.0301×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9000. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 1.75 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 20.4× (z +8.9) | [[Clobetasol propionate (drug)]] 5 µM 0.0301× (z -10.3) |
| [[PANC-1 (line)]] | alt | 5.16 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 12.9× (z +10.0) | — |
| [[SW480 (line)]] | alt | 1.43 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 56.8× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 11.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 9.18× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 1.37 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 36.7× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 0.708 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 62.5× (z +9.0) | — |
| [[A-172 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.923 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.609 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.285 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.259 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.869 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.776 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.665 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.998 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.236 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.377 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.219 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.437 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.307 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.598 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.880 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.272 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.212 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.349 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.927 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.248 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9000), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3GL3]] | +0.69 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[CALB2]] | +0.66 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[CIB1]] | +0.63 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[NDRG1]] | +0.62 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[UBA6]] | +0.62 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[WNT7B]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[WSCD1]] | +0.61 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[ANKRD37]] | +0.60 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[LHX1-DT]] | +0.60 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[DNAAF3]] | +0.58 | +0.36 / +0.53 | both halves | 1e-04 |  |
| [[TNFRSF11A]] | +0.58 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[PGPEP1]] | +0.57 | +0.46 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL1R1]] | -0.58 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[SUCLA2]] | -0.55 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[STXBP5]] | -0.55 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[ZFX]] | -0.54 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[UTP20]] | -0.53 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[DNAJC11]] | -0.53 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[CLHC1]] | -0.53 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[TCF12]] | -0.52 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[ANKRD17]] | -0.52 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[ZMYND11]] | -0.52 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[GTF3C6]] | -0.52 | -0.24 / -0.40 | both halves | 4e-04 |  |
| [[MCPH1]] | -0.52 | -0.34 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PI4K2A]] | B | C7orf57 activity raises PI4K2A's level | lines that do not express C7orf57 (18) vs lines expressing it (32) | 1.55× lower at baseline in the lines without C7orf57 | 0.050 | ⚠ within organs, on part of the lines; also absent: CACNG6, GNG11, PAPLN |
| [[STXBP5]] | B | C7orf57 activity lowers STXBP5's level | lines that do not express C7orf57 (18) vs lines expressing it (32) | 1.36× higher at baseline in the lines without C7orf57 | 0.059 | ⚠ within organs, on part of the lines; also absent: CACNG6, GNG11, PAPLN |
| [[ATG9B]] | B | C7orf57 activity raises ATG9B's level | lines that do not express C7orf57 (18) vs lines expressing it (32) | 1.65× lower at baseline in the lines without C7orf57 | 0.098 | ⚠ within organs, on part of the lines; also absent: CACNG6, GNG11, PAPLN |
| [[ZMYND11]] | B | C7orf57 activity lowers ZMYND11's level | lines that do not express C7orf57 (18) vs lines expressing it (32) | 1.26× higher at baseline in the lines without C7orf57 | 0.0995 | ⚠ within organs, on part of the lines; also absent: CACNG6, GNG11, PAPLN |
| [[LBH]] | C | C7orf57 activity raises LBH's level | lines that do not express C7orf57 (18) vs lines expressing it (32) | 3.25× lower at baseline in the lines without C7orf57 | 0.021 | ⚠ within organs, on part of the lines; also absent: CACNG6, GNG11, PAPLN; co-absent with the target |

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.5, -3.4); signed map (-4.0, 47.7). **Vector** length 52.1, 10.5% of its response variance represented; |z| ≥ 3 in 718 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.4 | +18.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.4 | +20.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +10.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.2 | +18.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +3.3 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -2.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 7 open reading frame 57 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p12.3 — chr7:48,035,511-48,061,304 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FCAP33 |
| Matched by | ensembl_id |

UniProt [Q8NEG2](https://www.uniprot.org/uniprotkb/Q8NEG2) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:22247](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22247) · Entrez [136288](https://www.ncbi.nlm.nih.gov/gene/136288) · UniProt [Q8NEG2](https://www.uniprot.org/uniprotkb/Q8NEG2) · Ensembl [ENSG00000164746](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164746)

## Data

Gene col 9000: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9000); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9000, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9000]; `tensor/DDL_lfc|DDL_z.npy` [9000]; `embed/gene_vectors.npy` [9000]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9000 or target_col == 9000). Every well: [[C7orf57 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C7orf57.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
