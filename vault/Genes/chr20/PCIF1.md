---
symbol: "PCIF1"
type: "gene"
col: 2052
ensembl_id: "ENSG00000100982"
name: "phosphorylated CTD interacting factor 1"
location: "20q13.12"
module: 153
arm: "+"
pooled_cpm: 7.97
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# PCIF1

*phosphorylated CTD interacting factor 1* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.11× (z +4.4, q 0.006, up in 4 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.50× (z +3.8, q 0.025, up in 12 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.490× (z -9.4, q 5e-18, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB11B]] (+0.64, fdr 1e-05), [[MED16]] (+0.60, fdr 1e-05), [[POLDIP3]] (+0.59, fdr 1e-05); moves opposite to [[TM4SF19-DYNLT2B]] (-0.56, fdr 5e-05), [[PFDN2]] (-0.50, fdr 4e-05), [[GBX1]] (-0.48, fdr 4e-05).
> It is in [[Module 153]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF215]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2052.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.4 | 0.006 | 4/48 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +4.1 | 0.012 | 13/40 (SW1417, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.50×** | +3.8 | 0.025 | 12/37 (A-427, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Salicylic acid (drug)]] 5 µM |  | 1.18× | +3.1 | 0.23 | 6/48 (Hs 766T, SHP-77, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.27× | +3.0 | 0.27 | 6/45 (LoVo, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2052.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.490×** | -9.4 | 5e-18 | 34/47 (PANC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.511×** | -8.8 | 4e-16 | 34/47 (NCI-H2030, C-33 A, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.531×** | -8.3 | 2e-14 | 28/47 (NCI-H2030, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.526×** | -8.1 | 8e-14 | 25/40 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.630×** | -6.1 | 1e-07 | 21/47 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.666×** | -5.3 | 9e-06 | 17/42 (LOX-IMVI, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.516×** | -4.5 | 5e-04 | 15/46 (A549, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.784×** | -4.5 | 5e-04 | 17/43 (NCI-H2030, A-172, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.716×** | -4.2 | 0.002 | 16/42 (NCI-H23, LS 180, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.740×** | -3.8 | 0.008 | 10/45 (HT-29, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.815×** | -3.8 | 0.008 | 13/48 (SW1417, NCI-H2030, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.588×** | -3.6 | 0.013 | 8/47 (NCI-H2030, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.762×** | -3.4 | 0.026 | 11/45 (J82, SW 900, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.787×** | -3.1 | 0.064 | 8/46 (H4, SW1417, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.787×** | -3.1 | 0.064 | 9/47 (MIA PaCa-2, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2052. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 9.71 | 0 | 2 (1 ⚠) | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0936× (z -11.1) |
| [[A-172 (line)]] | wt | 7.53 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -8.9) |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.130× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~86% of this change |
| [[HOP62 (line)]] | alt | 4.39 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0701× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~58% of this change |
| [[LOX-IMVI (line)]] | wt | 4.65 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0612× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -10.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW480 (line)]] | alt | 9.31 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.284× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[A-427 (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2052), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB11B]] | +0.64 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[MED16]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[POLDIP3]] | +0.59 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[ATP13A1]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[PIGO]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[USP19]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ARAF]] | +0.58 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ATXN7L2]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[HNRNPL]] | +0.55 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[TTC31]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[NCSTN]] | +0.55 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[IDH3G]] | +0.55 | +0.63 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TM4SF19-DYNLT2B]] | -0.56 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[PFDN2]] | -0.50 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[GBX1]] | -0.48 | -0.40 / -0.54 | both halves | 4e-05 |  |
| [[KCNK6]] | -0.48 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[DYNLT2B]] | -0.47 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[PRKRIP1]] | -0.46 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[FKBP11]] | -0.46 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[PPP1R14B]] | -0.45 | -0.31 / -0.38 | both halves | 2e-04 | same gene group |
| [[RASA2]] | -0.44 | -0.28 / -0.41 | both halves | 3e-04 |  |
| [[MAP2K1]] | -0.44 | -0.26 / -0.38 | both halves | 4e-04 |  |
| [[ARPC1B]] | -0.44 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[STK4]] | -0.44 | -0.33 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF215]] | B | ZNF215 activity lowers PCIF1's level | lines that do not express ZNF215 (12) vs lines expressing it (38) | 1.33× higher at baseline in the lines without ZNF215 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000283415, ENSG00000291143 |
| [[TOP2A]] | B | TOP2A activity raises PCIF1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.681). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.9, -20.6); signed map (-10.9, -31.5). **Vector** length 55.5, 7.26% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.8 | +4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -1.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.8 | +4.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +3.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.3 | +1.2 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.2 | +1.3 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -2.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.1 | -5.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.9 | -6.1 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.8 | -3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.6 | +0.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | phosphorylated CTD interacting factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:45,934,683-45,948,023 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA465L10.1, PPP1R121, CAPAM, MT-A70; previously C20orf67 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; 7BS N6-adenosine DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4Z3](https://www.uniprot.org/uniprotkb/Q9H4Z3) (mRNA):

> Cap-specific adenosine methyltransferase that catalyzes formation of N(6),2'-O-dimethyladenosine cap (m6A(m)) by methylating the adenosine at the second transcribed position of capped mRNAs. Recruited to the early elongation complex of RNA polymerase II (RNAPII) via interaction with POLR2A and mediates formation of m6A(m) co-transcriptionally.

**Summary**, from NCBI Gene [63935](https://www.ncbi.nlm.nih.gov/gene/63935):

> Enables RNA polymerase II C-terminal domain phosphoserine binding activity; S-adenosyl-L-methionine binding activity; and mRNA (2'-O-methyladenosine-N6-)-methyltransferase activity. Involved in mRNA processing; negative regulation of translation; and positive regulation of translation. Located in intercellular bridge; microtubule cytoskeleton; and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16200](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16200) · Entrez [63935](https://www.ncbi.nlm.nih.gov/gene/63935) · UniProt [Q9H4Z3](https://www.uniprot.org/uniprotkb/Q9H4Z3) · Ensembl [ENSG00000100982](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100982)

## Data

Gene col 2052: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2052); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2052, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2052]; `tensor/DDL_lfc|DDL_z.npy` [2052]; `embed/gene_vectors.npy` [2052]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2052 or target_col == 2052). Every well: [[PCIF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCIF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
