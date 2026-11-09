---
symbol: "ADAMTS4"
type: "gene"
col: 8199
ensembl_id: "ENSG00000158859"
name: "ADAM metallopeptidase with thrombospondin type 1 motif 4"
location: "1q23.3"
module: 84
arm: "+"
pooled_cpm: 5.07
n_lines_expressing: 11
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# ADAMTS4

*ADAM metallopeptidase with thrombospondin type 1 motif 4* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.08× (z +12.3, q 4e-32, up in 6 of 7 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.237×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0450×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.131×); [[Tofacitinib (drug)]] 5 µM in 1 line (C32 0.314×); [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.186×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNN4]] (+0.61, fdr 1e-05), [[LINC02509]] (+0.58, fdr 1e-05), [[PNP]] (+0.57, fdr 3e-05); moves opposite to [[SORBS2]] (-0.47, fdr 2e-04), [[TNRC6A]] (-0.46, fdr 1e-04), [[RDX]] (-0.45, fdr 1e-04).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[DCT]] → it (grade C ⚠); 2 go from it, the strongest it → [[PARVG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8199.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.08×** | +12.3 | 4e-32 | 6/7 (C32, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.38×** | +10.0 | 4e-21 | 1/5 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.76×** | +9.7 | 8e-20 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.08×** | +6.4 | 2e-08 | 3/8 (HS-578T, C32, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.44×** | +5.1 | 4e-05 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +3.7 | 0.019 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.74×** | +3.4 | 0.051 | 0/7 | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +3.3 | 0.065 | 2/7 (C32, HepG2/C3A) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.70×** | +3.3 | 0.065 | 1/7 (C32) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.078 | 1/8 (HS-578T) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.16×** | +3.2 | 0.078 | 1/6 (MIA PaCa-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.66×** | +3.1 | 0.085 | 2/8 (RPMI-7951, HS-578T) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8199.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.237×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0450×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.131×); [[Tofacitinib (drug)]] 5 µM in 1 line (C32 0.314×); [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.186×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.523× | -3.7 | 0.11 | 0/8 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8199. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 35.7 | 0 | 4 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.237× (z -18.2) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -10.4) |
| [[C32 (line)]] | wt | 102 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +11.5) | [[Tofacitinib (drug)]] 5 µM 0.314× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 6.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 93.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.556 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.644 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.811 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.555 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.517 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.770 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.770 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.528 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.974 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.482 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.912 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.551 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.684 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.764 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8199), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNN4]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[LINC02509]] | +0.58 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[PNP]] | +0.57 | +0.46 / +0.56 | both halves | 3e-05 | pathway: Diseases of metabolism |
| [[KCNC4]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[NPAS1]] | +0.56 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[SH2B3]] | +0.55 | +0.54 / +0.37 | both halves | 8e-05 |  |
| [[GLDC]] | +0.55 | +0.57 / +0.36 | both halves | 1e-04 |  |
| [[CPNE5]] | +0.54 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[PINLYP]] | +0.54 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[RHBDF2]] | +0.53 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[WT1-AS]] | +0.53 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[PARVG]] | +0.53 | +0.49 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SORBS2]] | -0.47 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[TNRC6A]] | -0.46 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[RDX]] | -0.45 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[LSM14A]] | -0.44 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[FIGN]] | -0.44 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[NR1D2]] | -0.43 | -0.47 / -0.29 | both halves | 3e-04 |  |
| [[RNF115]] | -0.43 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[DIS3L]] | -0.42 | -0.30 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCT]] | C | DCT activity raises ADAMTS4's level | lines that do not express DCT (42) vs lines expressing it (8) | 3.67× lower at baseline in the lines without DCT | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1; co-absent with the target |
| [[ROBO4]] | C | ROBO4 activity raises ADAMTS4's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.81× lower at baseline in the lines without ROBO4 | 0.048 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1; co-absent with the target |
| [[MIR3681HG]] | C | MIR3681HG activity raises ADAMTS4's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 2.45× lower at baseline in the lines without MIR3681HG | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARVG]] | B | ADAMTS4 activity raises PARVG's level | lines that do not express ADAMTS4 (39) vs lines expressing it (11) | 1.99× lower at baseline in the lines without ADAMTS4 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: FCRLA, APOA2, A2M |
| [[MIR3681HG]] | C | ADAMTS4 activity raises MIR3681HG's level | lines that do not express ADAMTS4 (39) vs lines expressing it (11) | 3.38× lower at baseline in the lines without ADAMTS4 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: FCRLA, APOA2, A2M; co-absent with the target |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.580). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (53.0, 3.5); signed map (7.0, 56.1). **Vector** length 26.6, 7.28% of its response variance represented; |z| ≥ 3 in 255 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.6 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.2 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.2 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +0.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +0.7 | +1.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.7 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +0.7 | +2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +0.6 | +1.9 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.9 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.9 | -1.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase with thrombospondin type 1 motif 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:161,184,302-161,199,054 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0688, ADAMTS-2, ADMP-1 |
| Gene groups (HGNC) | ADAM metallopeptidases with thrombospondin type 1 motif |
| Reactome | 8 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O75173](https://www.uniprot.org/uniprotkb/O75173) (A disintegrin and metalloproteinase with thrombospondin motifs 4):

> Cleaves aggrecan, a cartilage proteoglycan, at the '392-Glu-|-Ala-393' site and may be involved in its turnover. Also cleaves COMP. May play an important role in the destruction of aggrecan in arthritic diseases. Could be a critical factor in the exacerbation of neurodegeneration in Alzheimer disease.

**Summary**, from NCBI Gene [9507](https://www.ncbi.nlm.nih.gov/gene/9507):

> This gene encodes a member of the ADAMTS (a disintegrin and metalloproteinase with thrombospondin motifs) protein family. Members of this family share several distinct protein modules, including a propeptide region, a metalloproteinase domain, a disintegrin-like domain, and a thrombospondin type 1 (TS) motif. Individual members of this family differ in the number of C-terminal TS motifs, and some have unique C-terminal domains. The enzyme encoded by this gene lacks a C-terminal TS motif. The …

**Accessions** — [HGNC:220](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:220) · Entrez [9507](https://www.ncbi.nlm.nih.gov/gene/9507) · UniProt [O75173](https://www.uniprot.org/uniprotkb/O75173) · Ensembl [ENSG00000158859](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158859)

## Data

Gene col 8199: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8199); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8199, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8199]; `tensor/DDL_lfc|DDL_z.npy` [8199]; `embed/gene_vectors.npy` [8199]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8199 or target_col == 8199). Every well: [[ADAMTS4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTS4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
