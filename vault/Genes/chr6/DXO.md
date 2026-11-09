---
symbol: "DXO"
type: "gene"
col: 12855
ensembl_id: "ENSG00000204348"
name: "decapping exoribonuclease"
location: "6p21.33"
module: 96
arm: "+"
pooled_cpm: 3.44
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# DXO

*decapping exoribonuclease* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.98× (z +10.2, q 1e-21, up in 27 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.453× (z -8.4, q 4e-14, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF213]] (+0.76, fdr 1e-05), [[C19orf54]] (+0.76, fdr 1e-05), [[STK16]] (+0.73, fdr 1e-05); moves opposite to [[ARPC1B]] (-0.59, fdr 3e-05), [[TXN]] (-0.58, fdr 1e-05), [[BRI3BP]] (-0.56, fdr 3e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12855.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +10.2 | 1e-21 | 27/35 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +9.3 | 3e-18 | 4/9 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +7.0 | 5e-10 | 6/17 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +7.0 | 5e-10 | 7/10 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.87×** | +6.4 | 2e-08 | 21/41 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +4.5 | 7e-04 | 6/21 (SW1417, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +3.9 | 0.009 | 12/34 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.64×** | +3.7 | 0.013 | 2/20 (NCI-H460, LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.013 | 4/45 (J82, BT-474, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.59×** | +3.5 | 0.026 | 4/34 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.86×** | +3.4 | 0.033 | 6/38 (LoVo, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pemigatinib (drug)]] 0.05 µM |  | **1.40×** | +3.3 | 0.042 | 7/42 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12855.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.453×** | -8.4 | 4e-14 | 30/46 (AsPC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.515×** | -7.0 | 7e-10 | 29/45 (HepG2/C3A, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.545×** | -6.4 | 3e-08 | 27/46 (RPMI-7951, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.638×** | -4.7 | 3e-04 | 10/46 (HS-578T, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.737×** | -4.6 | 6e-04 | 15/44 (A-427, LS 180, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.679×** | -4.1 | 0.004 | 14/44 (C-33 A, C32, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12855. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +8.6) | — |
| [[KATO III (line)]] | alt | 5.04 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.05 µM 0.0430× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 7.73 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.145× (z -8.9) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 2.11 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0672× (z -9.0) |
| [[A-172 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12855), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF213]] | +0.76 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[C19orf54]] | +0.76 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[STK16]] | +0.73 | +0.77 / +0.55 | both halves | 1e-05 |  |
| [[PAN2]] | +0.73 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[MBD6]] | +0.70 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[PRR14]] | +0.70 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[AMZ2P1-1]] | +0.69 | +0.78 / +0.50 | both halves | 1e-05 |  |
| [[PBX2]] | +0.69 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[DTX3]] | +0.68 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[CDK3]] | +0.68 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[CIRBP]] | +0.68 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[CNOT3]] | +0.67 | +0.69 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARPC1B]] | -0.59 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[TXN]] | -0.58 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[BRI3BP]] | -0.56 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[NME2]] | -0.56 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[NHP2]] | -0.56 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[HACD3]] | -0.55 | -0.57 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DXO's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises DXO's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PPP1R37]] | C | PPP1R37's natural level weakens DXO's drug response | PPP1R37's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.18; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.708). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-12.2, 5.8); signed map (11.7, -19.5). **Vector** length 51.7, 6.39% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +7.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +3.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +2.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.5 | +2.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.9 | -8.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.6 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.2 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | decapping exoribonuclease |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,969,810-31,972,290 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DOM3L; previously DOM3Z |
| Reactome | 2 pathways, smallest: Nuclear RNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O77932](https://www.uniprot.org/uniprotkb/O77932) (Decapping and exoribonuclease protein):

> Decapping enzyme for NAD-capped RNAs: specifically hydrolyzes the nicotinamide adenine dinucleotide (NAD) cap from a subset of RNAs by removing the entire NAD moiety from the 5'-end of an NAD-capped RNA. The NAD-cap is present at the 5'-end of some RNAs and snoRNAs. In contrast to the canonical 5'-end N7 methylguanosine (m7G) cap, the NAD cap promotes mRNA decay. Preferentially acts on NAD-capped transcripts in response to environmental stress. Also acts as a non-canonical decapping enzyme that …

**Summary**, from NCBI Gene [1797](https://www.ncbi.nlm.nih.gov/gene/1797):

> This gene localizes to the major histocompatibility complex (MHC) class III region on chromosome 6. The function of its protein product is unknown, but its ubiquitous expression and conservation in both simple and complex eukaryotes suggests that this may be a housekeeping gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2992](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2992) · Entrez [1797](https://www.ncbi.nlm.nih.gov/gene/1797) · UniProt [O77932](https://www.uniprot.org/uniprotkb/O77932) · Ensembl [ENSG00000204348](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204348)

## Data

Gene col 12855: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12855); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12855, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12855]; `tensor/DDL_lfc|DDL_z.npy` [12855]; `embed/gene_vectors.npy` [12855]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12855 or target_col == 12855). Every well: [[DXO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DXO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
