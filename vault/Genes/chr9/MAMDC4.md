---
symbol: "MAMDC4"
type: "gene"
col: 10878
ensembl_id: "ENSG00000177943"
name: "MAM domain containing 4"
location: "9q34.3"
module: 157
arm: "+"
pooled_cpm: 3.31
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# MAMDC4

*MAM domain containing 4* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 1.94× (z +5.2, q 1e-04, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.499× (z -5.9, q 2e-06, down in 22 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIDD1]] (+0.65, fdr 1e-05), [[PHPT1]] (+0.61, fdr 2e-05, ⚠ read-through risk), [[FDXR]] (+0.60, fdr 2e-05), [[CFAP410]] (+0.57, fdr 1e-05); moves opposite to [[CBX3]] (-0.49, fdr 8e-05), [[CCT6A]] (-0.47, fdr 4e-05), [[KIF2A]] (-0.47, fdr 4e-05).
> It is in [[Module 157]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CDC42BPG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10878.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +5.2 | 1e-04 | 0/6 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +4.9 | 2e-04 | 2/4 (PANC-1, HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +4.1 | 0.008 | 5/17 (NCI-H1792, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +3.9 | 0.012 | 5/22 (A498, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +3.4 | 0.072 | 1/4 (PANC-1) | rises with dose | noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.70× | +3.2 | 0.12 | 5/20 (LoVo, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.44× | +3.1 | 0.14 | 5/31 (PANC-1, LS 180, …) | inconsistent across doses | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.44× | +3.1 | 0.14 | 6/30 (A549, A-172, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, none with an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10878.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.499×** | -5.9 | 2e-06 | 22/44 (C32, LoVo, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.510×** | -5.7 | 3e-06 | 26/45 (SW48, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.539×** | -5.2 | 3e-05 | 22/42 (HCT15, SNU-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.526×** | -5.1 | 4e-05 | 22/41 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.566×** | -4.8 | 2e-04 | 16/44 (COLO 205, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.580×** | -4.6 | 4e-04 | 19/43 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.596×** | -4.4 | 9e-04 | 16/45 (NCI-H1792, LoVo, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.607×** | -4.2 | 0.002 | 18/45 (SK-MEL-2, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.395×** | -4.1 | 0.002 | 8/40 (HOP62, HCT15, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.437×** | -3.7 | 0.014 | 12/43 (CFPAC-1, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Penfluridol (drug)]] 5 µM |  | **0.654×** | -3.5 | 0.027 | 12/42 (SHP-77, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.744×** | -3.4 | 0.027 | 13/36 (SNU-423, C32, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.680×** | -3.3 | 0.047 | 10/37 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.486×** | -3.2 | 0.056 | 13/35 (SK-MEL-2, NCI-H1792, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.694×** | -3.1 | 0.074 | 11/43 (C-33 A, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10878. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 5.39 | 0 | 2 (1 ⚠) | — | [[Ligustrazine (drug)]] 5 µM 0.0603× (z -11.1) |
| [[A-172 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10878), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIDD1]] | +0.65 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[PHPT1]] | +0.61 | +0.48 / +0.68 | both halves | 2e-05 | STRING 425; ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of PHPT1 on the same strand (can correlate by spillover, not regulation) |
| [[FDXR]] | +0.60 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[CFAP410]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[MIB2]] | +0.53 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[AJM1]] | +0.53 | +0.49 / +0.54 | both halves | 1e-05 | ⚠ same locus (2.1 kb, same strand: neighbours can correlate without regulation) |
| [[CDK3]] | +0.52 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[RHOT2]] | +0.52 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[CIC]] | +0.52 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[CDIP1]] | +0.52 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[GOLGA8A]] | +0.52 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[DGAT1]] | +0.51 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[PLXNB2]] | +0.51 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[HNRNPH1]] | +0.51 | +0.49 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBX3]] | -0.49 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[CCT6A]] | -0.47 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[KIF2A]] | -0.47 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[HSPD1]] | -0.46 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[CCT3]] | -0.45 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[PTGES3]] | -0.45 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[NIN]] | -0.43 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[CCT4]] | -0.43 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[CCT5]] | -0.43 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[TCP1]] | -0.43 | -0.32 / -0.45 | both halves | 1e-04 |  |
| [[GGCT]] | -0.42 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[ARPC5]] | -0.42 | -0.30 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC42BPG]] | B | CDC42BPG activity lowers MAMDC4's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.33× higher at baseline in the lines without CDC42BPG | 0.083 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.578). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-14.2, -25.7); signed map (-0.5, 4.4). **Vector** length 48.1, 5.87% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.6 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.0 | +3.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +3.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +2.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.6 | +2.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.2 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.4 | -4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -3.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.3 | -1.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | MAM domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,850,943-136,860,799 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AEGP, DKFZp434M1411, EDTB |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UXC1](https://www.uniprot.org/uniprotkb/Q6UXC1) (Apical endosomal glycoprotein):

> Probably involved in the sorting and selective transport of receptors and ligands across polarized epithelia.

**Summary**, from NCBI Gene [158056](https://www.ncbi.nlm.nih.gov/gene/158056):

> Predicted to enable protein histidine phosphatase activity. Predicted to be involved in nervous system development. Predicted to act upstream of or within Wnt signaling pathway and protein localization to nucleus. Predicted to be located in cytosol. Predicted to be part of Wnt signalosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24083](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24083) · Entrez [158056](https://www.ncbi.nlm.nih.gov/gene/158056) · UniProt [Q6UXC1](https://www.uniprot.org/uniprotkb/Q6UXC1) · Ensembl [ENSG00000177943](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177943)

## Data

Gene col 10878: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10878); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10878, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10878]; `tensor/DDL_lfc|DDL_z.npy` [10878]; `embed/gene_vectors.npy` [10878]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10878 or target_col == 10878). Every well: [[MAMDC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAMDC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
