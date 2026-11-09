---
symbol: "NMB"
type: "gene"
col: 12442
ensembl_id: "ENSG00000197696"
name: "neuromedin B"
location: "15q25.2"
module: 24
arm: "+"
pooled_cpm: 5.35
n_lines_expressing: 44
n_dd_up: 7
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# NMB

*neuromedin B* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.35× (z +7.4, q 9e-11, up in 24 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 12.8×).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.458× (z -4.8, q 0.001, down in 19 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RABAC1]] (+0.62, fdr 1e-05), [[MIEN1]] (+0.61, fdr 1e-05), [[BLVRB]] (+0.61, fdr 1e-05); moves opposite to [[FARSB]] (-0.56, fdr 2e-05), [[ATIC]] (-0.55, fdr 1e-05), [[LAS1L]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CXCR4]] → it (grade B ⚠); 2 go from it, the strongest it → [[TUBA4A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12442.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 12.8×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +7.4 | 9e-11 | 24/35 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.72×** | +5.9 | 1e-06 | 19/27 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.32×** | +5.1 | 5e-05 | 11/22 (NCI-H2030, LoVo, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.00×** | +4.2 | 0.003 | 15/31 (NCI-H460, COLO 205, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.03×** | +4.1 | 0.004 | 3/11 (NCI-H2030, HT-29, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.85×** | +3.7 | 0.017 | 13/27 (A-172, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.79×** | +3.3 | 0.084 | 5/15 (NCI-H2030, PANC-1, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.65× | +3.1 | 0.16 | 15/39 (COLO 205, KATO III, …) | two highest doses |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.64× | +3.0 | 0.16 | 12/33 (NCI-H2030, KATO III, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12442.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.458×** | -4.8 | 0.001 | 19/33 (CFPAC-1, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.515×** | -4.0 | 0.015 | 20/40 (Panc 03.27, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.658×** | -3.6 | 0.061 | 15/36 (MIA PaCa-2, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 5 µM |  | 0.577× | -3.3 | 0.12 | 17/40 (hTERT-HPNE, SNU-423, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.357× | -3.3 | 0.12 | 13/37 (LoVo, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.368× | -3.2 | 0.14 | 17/32 (SW1417, KATO III, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12442. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 3.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +11.1) | — |
| [[BT-474 (line)]] | alt | 16.9 | 0 | 1 | — | [[Afatinib (drug)]] 5 µM 0.0781× (z -9.5) |
| [[A-172 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.376 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.979 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.774 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.873 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.538 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12442), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABAC1]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[MIEN1]] | +0.61 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[BLVRB]] | +0.61 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[IER5L]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[FTL]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[APOC1]] | +0.57 | +0.34 / +0.62 | both halves | 1e-04 |  |
| [[MIR4458HG]] | +0.57 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[NPC2]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[NENF]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[PPP2R3A]] | +0.56 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[CUTA]] | +0.56 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[ATP6V0B]] | +0.55 | +0.37 / +0.57 | both halves | 7e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FARSB]] | -0.56 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[ATIC]] | -0.55 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[LAS1L]] | -0.54 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[PYGB]] | -0.53 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[TRMT6]] | -0.53 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[NCBP1]] | -0.53 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[RUVBL1]] | -0.52 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[GNL3L]] | -0.52 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[BCL2L1]] | -0.51 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[HNRNPD]] | -0.51 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[SYNCRIP]] | -0.50 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[LARS1]] | -0.50 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCR4]] | B | CXCR4 activity raises NMB's level | lines that do not express CXCR4 (22) vs lines expressing it (28) | 1.53× lower at baseline in the lines without CXCR4 | 0.073 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, LMO2 |
| [[TUBA4A]] | B | TUBA4A activity raises NMB's level | lines that do not express TUBA4A (13) vs lines expressing it (37) | 1.63× lower at baseline in the lines without TUBA4A | 0.094 | ⚠ within organs, on part of the lines; also absent: TNK1, ETV7, CDCP1; maybe low, not absent |
| [[ENO2]] | C | ENO2 activity raises NMB's level | lines that do not express ENO2 (3) vs lines expressing it (47) | 3.01× lower at baseline in the lines without ENO2 | 0.087 | ⚠ few lines (3 vs 47); across organs; also absent: NMB; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TUBA4A]] | B | NMB activity raises TUBA4A's level | lines that do not express NMB (6) vs lines expressing it (44) | 1.93× lower at baseline in the lines without NMB | 0.060 | ⚠ within organs, on part of the lines; also absent: ENO2, ARFGEF3, STAT5A; maybe low, not absent; its own permutation p |
| [[PDE8A]] | B | NMB activity raises PDE8A's level | lines that do not express NMB (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without NMB | 0.060 | ⚠ within organs, on part of the lines; also absent: ENO2, ARFGEF3, STAT5A; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.573). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.3, -25.1); signed map (-26.2, 9.5). **Vector** length 69.0, 14.9% of its response variance represented; |z| ≥ 3 in 713 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +7.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.2 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +2.3 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.1 | +0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +1.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | -4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.0 | -4.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | neuromedin B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.2 — chr15:84,655,129-84,658,563 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2277, MGC3936, MGC17211 |
| Reactome | 6 pathways, smallest: Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P08949](https://www.uniprot.org/uniprotkb/P08949) (Neuromedin-B):

> Stimulates smooth muscle contraction (By similarity). Induces sighing by acting directly on the pre-Botzinger complex, a cluster of several thousand neurons in the ventrolateral medulla responsible for inspiration during respiratory activity (By similarity). Contributes to the induction of sneezing following exposure to chemical irritants or allergens which causes release of NMB by nasal sensory neurons and activation of NMBR-expressing neurons in the sneeze-evoking region of the brainstem (By …

**Summary**, from NCBI Gene [4828](https://www.ncbi.nlm.nih.gov/gene/4828):

> This gene encodes a member of the bombesin-like family of neuropeptides, which negatively regulate eating behavior. The encoded protein may regulate colonic smooth muscle contraction through binding to its cognate receptor, the neuromedin B receptor (NMBR). Polymorphisms of this gene may be associated with hunger, weight gain and obesity. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2015]

**Accessions** — [HGNC:7842](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7842) · Entrez [4828](https://www.ncbi.nlm.nih.gov/gene/4828) · UniProt [P08949](https://www.uniprot.org/uniprotkb/P08949) · Ensembl [ENSG00000197696](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197696)

## Data

Gene col 12442: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12442); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12442, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12442]; `tensor/DDL_lfc|DDL_z.npy` [12442]; `embed/gene_vectors.npy` [12442]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12442 or target_col == 12442). Every well: [[NMB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NMB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
