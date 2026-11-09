---
symbol: "SNAP91"
type: "gene"
col: 796
ensembl_id: "ENSG00000065609"
name: "synaptosome associated protein 91"
location: "6q14.2"
module: 61
arm: "+"
pooled_cpm: 2.19
n_lines_expressing: 24
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 6
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# SNAP91

*synaptosome associated protein 91* — 6q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.78× (z +15.9, q 0e+00, up in 8 of 12 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Monocrotaline (drug)]] 5 µM in 1 line (A549 0.0602×); [[Digitoxin (drug)]] 5 µM in 1 line (A549 0.0763×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (J82 0.177×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPM6A]] (+0.70, fdr 7e-06), [[CCDC85A]] (+0.69, fdr 7e-06), [[ERC2]] (+0.65, fdr 7e-06); moves opposite to [[EFCAB11]] (-0.48, fdr 4e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 6 go from it, the strongest it → [[CHMP2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 796.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.78×** | +15.9 | 0e+00 | 8/12 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.57×** | +11.9 | 5e-30 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **3.04×** | +11.3 | 3e-27 | 15/16 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.50×** | +9.3 | 2e-18 | 7/12 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.18×** | +8.3 | 1e-14 | 2/8 (PANC-1, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.36×** | +8.1 | 8e-14 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.64×** | +7.0 | 2e-10 | 14/15 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.09×** | +5.3 | 8e-06 | 5/15 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.60×** | +4.9 | 6e-05 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +4.6 | 2e-04 | 4/13 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.21×** | +4.1 | 0.003 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.005 | 1/16 (NCI-H23) | top dose only | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.68×** | +3.7 | 0.009 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +3.7 | 0.009 | 2/10 (NCI-H460, A549) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.67×** | +3.7 | 0.009 | 2/15 (NCI-H460, SHP-77) | two highest doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.62×** | +3.4 | 0.019 | 0/16 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +3.4 | 0.022 | 9/17 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +3.2 | 0.038 | 1/11 (NCI-H460) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.039 | 1/14 (NCI-H1573) | top dose only |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.58×** | +3.0 | 0.063 | 0/8 | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Monocrotaline (drug)]] 5 µM in 1 line (A549 0.0602×); [[Digitoxin (drug)]] 5 µM in 1 line (A549 0.0763×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (J82 0.177×; ⚠ toxic; transcription drop).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 796. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 0.981 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 130× (z +12.8) | — |
| [[A549 (line)]] | wt | 4.98 | 0 | 2 (1 ⚠) | — | [[Monocrotaline (drug)]] 5 µM 0.0602× (z -9.2) |
| [[J82 (line)]] | alt | 14.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 1.29 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 16.8× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 0.991 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 15.7× (z +9.2) | — |
| [[A-427 (line)]] | wt | 0.807 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.385 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.753 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.514 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.457 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.518 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.475 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.427 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.395 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.972 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.679 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.505 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.431 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 796), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPM6A]] | +0.70 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[CCDC85A]] | +0.69 | +0.63 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[ERC2]] | +0.65 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[KCNH1]] | +0.62 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[NRXN1]] | +0.62 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[CELF4]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[XKR4]] | +0.61 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[DACH2]] | +0.60 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[SGCZ]] | +0.60 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[LINC02511]] | +0.60 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[SNTG2]] | +0.60 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[HS6ST3]] | +0.59 | +0.59 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB11]] | -0.48 | -0.42 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHMP2B]] | B | SNAP91 activity lowers CHMP2B's level | lines that do not express SNAP91 (26) vs lines expressing it (24) | 1.42× higher at baseline in the lines without SNAP91 | 0.092 | ⚠ within organs, on part of the lines; also absent: CHST8, PLEKHG4B, COLEC12; maybe low, not absent |
| [[COLEC12]] | C | SNAP91 activity raises COLEC12's level | lines that do not express SNAP91 (26) vs lines expressing it (24) | 2.99× lower at baseline in the lines without SNAP91 | 0.050 | ⚠ within organs, on part of the lines; also absent: CHST8, PLEKHG4B, COLEC12; maybe low, not absent; co-absent with the target |
| [[NUDT11]] | C | SNAP91 activity raises NUDT11's level | lines that do not express SNAP91 (26) vs lines expressing it (24) | 2.05× lower at baseline in the lines without SNAP91 | 0.077 | ⚠ within organs, on part of the lines; also absent: CHST8, PLEKHG4B, COLEC12; maybe low, not absent; co-absent with the target |
| [[AFF2]] | C | SNAP91 activity raises AFF2's level | lines that do not express SNAP91 (26) vs lines expressing it (24) | 2.02× lower at baseline in the lines without SNAP91 | 0.080 | ⚠ within organs, on part of the lines; also absent: CHST8, PLEKHG4B, COLEC12; maybe low, not absent; co-absent with the target |
| [[CHST8]] | C | SNAP91 activity raises CHST8's level | lines that do not express SNAP91 (26) vs lines expressing it (24) | 3.43× lower at baseline in the lines without SNAP91 | 0.089 | ⚠ within organs, on part of the lines; also absent: CHST8, PLEKHG4B, COLEC12; maybe low, not absent; co-absent with the target |
| [[RET]] | C | SNAP91 activity raises RET's level | lines that do not express SNAP91 (26) vs lines expressing it (24) | 2.46× lower at baseline in the lines without SNAP91 | 0.091 | ⚠ within organs, on part of the lines; also absent: CHST8, PLEKHG4B, COLEC12; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.737). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.8, 30.8); signed map (32.6, 21.3). **Vector** length 36.5, 8.27% of its response variance represented; |z| ≥ 3 in 390 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +11.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -1.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -0.3 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.9 | -2.6 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | synaptosome associated protein 91 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.2 — chr6:83,552,880-83,709,691 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0656, AP180, CALM |
| Hallmark sets | SPERMATOGENESIS, KRAS_SIGNALING_UP |
| Reactome | 4 pathways, smallest: Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [O60641](https://www.uniprot.org/uniprotkb/O60641) (Clathrin coat assembly protein AP180):

> Adaptins are components of the adapter complexes which link clathrin to receptors in coated vesicles. Clathrin-associated protein complexes are believed to interact with the cytoplasmic tails of membrane proteins, leading to their selection and concentration. Binding of AP180 to clathrin triskelia induces their assembly into 60-70 nm coats (By similarity).

**Summary**, from NCBI Gene [9892](https://www.ncbi.nlm.nih.gov/gene/9892):

> Predicted to enable several functions, including clathrin heavy chain binding activity; clathrin-cargo adaptor activity; and phospholipid binding activity. Acts upstream of or within regulation of clathrin-dependent endocytosis. Predicted to be located in cytosol; postsynaptic density; and synaptic membrane. Predicted to be active in several cellular components, including Schaffer collateral - CA1 synapse; cytoplasmic vesicle; and parallel fiber to Purkinje cell synapse. Predicted to be …

**Accessions** — [HGNC:14986](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14986) · Entrez [9892](https://www.ncbi.nlm.nih.gov/gene/9892) · UniProt [O60641](https://www.uniprot.org/uniprotkb/O60641) · Ensembl [ENSG00000065609](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065609)

## Data

Gene col 796: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 796); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 796, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 796]; `tensor/DDL_lfc|DDL_z.npy` [796]; `embed/gene_vectors.npy` [796]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 796 or target_col == 796). Every well: [[SNAP91 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNAP91.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
