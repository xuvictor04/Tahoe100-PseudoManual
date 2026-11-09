---
symbol: "SDR39U1"
type: "gene"
col: 1965
ensembl_id: "ENSG00000100445"
name: "short chain dehydrogenase/reductase family 39U member 1"
location: "14q12"
module: 96
arm: "+"
pooled_cpm: 7.32
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# SDR39U1

*short chain dehydrogenase/reductase family 39U member 1* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.54× (z +7.8, q 2e-12, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.768× (z -4.8, q 7e-04, down in 26 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Simotinib (drug)]] 5 µM in 1 line (NCI-H23 0.0726×; ⚠ toxic); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.134×; ⚠ cell-cycle shift, explains ~22% of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0670×); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (HCT15 0.0726×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (C-33 A 0.0755×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DXO]] (+0.64, fdr 1e-05), [[CZIB]] (+0.63, fdr 1e-05), [[PRR14]] (+0.61, fdr 1e-05); moves opposite to [[ARPC1B]] (-0.52, fdr 4e-05), [[CBX3]] (-0.47, fdr 4e-05), [[NME2]] (-0.46, fdr 4e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TRIP6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1965.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +7.8 | 2e-12 | 31/47 (A498, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +6.9 | 2e-09 | 21/33 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +6.2 | 1e-07 | 3/14 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.63×** | +5.8 | 1e-06 | 10/22 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +5.5 | 4e-06 | 15/35 (NCI-H2347, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.29×** | +4.6 | 5e-04 | 15/43 (NCI-H2030, AsPC-1, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +4.3 | 0.001 | 16/45 (A-427, LS 180, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +3.9 | 0.006 | 9/36 (A498, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.64×** | +3.8 | 0.008 | 11/37 (Panc 03.27, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.84×** | +3.7 | 0.011 | 3/37 (A498, A549, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.6 | 0.019 | 4/21 (KATO III, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.022 | 11/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.54×** | +3.3 | 0.036 | 5/43 (Panc 03.27, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1965.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Simotinib (drug)]] 5 µM in 1 line (NCI-H23 0.0726×; ⚠ toxic); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.134×; ⚠ cell-cycle shift, explains ~22% of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0670×); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (HCT15 0.0726×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (C-33 A 0.0755×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.768×** | -4.8 | 7e-04 | 26/43 (A549, NCI-H23, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | 0.766× | -3.5 | 0.12 | 14/47 (NCI-H2030, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.769× | -3.4 | 0.12 | 12/47 (SW 1271, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Menadione (drug)]] 0.05 µM |  | 0.768× | -3.2 | 0.22 | 12/43 (HepG2/C3A, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1965. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 12.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -11.3) ⚠ cell-cycle shift, explains ~22% of this change |
| [[C-33 A (line)]] | alt | 12.4 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0755× (z -10.1) |
| [[HCT15 (line)]] | alt | 13.6 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0726× (z -10.9) |
| [[Hs 766T (line)]] | wt | 4.96 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.0856× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 4.80 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0997× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 9.69 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0726× (z -11.8) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 7.50 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0670× (z -11.2) |
| [[A-172 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1965), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DXO]] | +0.64 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[CZIB]] | +0.63 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[PRR14]] | +0.61 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ACP2]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[WDR6]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[MBD6]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[DEDD]] | +0.57 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[PIGO]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[DECR2]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 | same gene group |
| [[SRSF6]] | +0.56 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[FASTK]] | +0.55 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[KDM5D]] | +0.55 | +0.37 / +0.52 | both halves | 9e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARPC1B]] | -0.52 | -0.40 / -0.56 | both halves | 4e-05 |  |
| [[CBX3]] | -0.47 | -0.43 / -0.46 | both halves | 4e-05 |  |
| [[NME2]] | -0.46 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[BCAP31]] | -0.46 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[SENP5]] | -0.46 | -0.36 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIP6]] | B | TRIP6 activity lowers SDR39U1's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.38× higher at baseline in the lines without TRIP6 | 0.044 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-28.4, 17.6); signed map (6.5, -21.4). **Vector** length 50.5, 6.33% of its response variance represented; |z| ≥ 3 in 736 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.2 | +7.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +5.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.8 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +6.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +3.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +3.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +2.4 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.8 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.9 | -2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.8 | -4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.5 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Adenosine (drug)]] 0.5 µM |  | -1.3 | -1.8 |
|  | [[Rifaximin (drug)]] 5 µM |  | -1.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | short chain dehydrogenase/reductase family 39U member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,439,766-24,442,905 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HCDI; previously C14orf124 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRG7](https://www.uniprot.org/uniprotkb/Q9NRG7) (Epimerase family protein SDR39U1):

> Putative NADP-dependent oxidoreductase.

**Summary**, from NCBI Gene [56948](https://www.ncbi.nlm.nih.gov/gene/56948):

> This gene encodes a member of the short-chain dehydrogenases/reductases (SDR) superfamily, which includes both classical and extended types. The encoded protein represents an extended type, with similarity to epimerases. Alternatively spliced transcript variants that encode different protein isoforms have been described. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:20275](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20275) · Entrez [56948](https://www.ncbi.nlm.nih.gov/gene/56948) · UniProt [Q9NRG7](https://www.uniprot.org/uniprotkb/Q9NRG7) · Ensembl [ENSG00000100445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100445)

## Data

Gene col 1965: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1965); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1965, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1965]; `tensor/DDL_lfc|DDL_z.npy` [1965]; `embed/gene_vectors.npy` [1965]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1965 or target_col == 1965). Every well: [[SDR39U1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDR39U1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
