---
symbol: "SPSB2"
type: "gene"
col: 3258
ensembl_id: "ENSG00000111671"
name: "splA/ryanodine receptor domain and SOCS box containing 2"
location: "12p13.31"
module: 93
arm: "+"
pooled_cpm: 4.34
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# SPSB2

*splA/ryanodine receptor domain and SOCS box containing 2* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.03× (z +8.9, q 4e-16, up in 32 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.618× (z -4.2, q 0.012, down in 21 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC23]] (+0.76, fdr 7e-06, ⚠ same locus), [[DHDH]] (+0.72, fdr 7e-06), [[DALRD3]] (+0.71, fdr 7e-06), [[IFRD1]] (+0.67, fdr 1e-05); moves opposite to [[PTAR1]] (-0.64, fdr 1e-05), [[RFT1]] (-0.61, fdr 1e-05), [[NHLRC2]] (-0.60, fdr 3e-04).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EFNA2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MED26]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3258.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +8.9 | 4e-16 | 32/37 (HOP62, AsPC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.88×** | +5.6 | 5e-06 | 20/43 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +5.3 | 2e-05 | 2/7 (SNU-423, CFPAC-1) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.69×** | +4.7 | 4e-04 | 6/22 (SW480, SW 900, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.66×** | +4.5 | 8e-04 | 11/23 (SW1417, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.036 | 8/37 (hTERT-HPNE, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | 1.47× | +3.2 | 0.12 | 2/31 (A-427, SW480) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.28× | +3.1 | 0.12 | 12/37 (COLO 205, C32, …) | top dose only | composition shift |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.42× | +3.1 | 0.12 | 10/39 (C32, HS-578T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.41× | +3.1 | 0.12 | 10/47 (SW480, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.41× | +3.0 | 0.12 | 8/47 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3258.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.618×** | -4.2 | 0.012 | 21/44 (BT-474, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.643×** | -3.9 | 0.028 | 18/43 (HepG2/C3A, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.670×** | -3.5 | 0.079 | 15/47 (A-427, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.689× | -3.3 | 0.14 | 15/43 (NCI-H2030, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3258. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -10.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[AsPC-1 (line)]] | alt | 2.71 | 0 | 1 (1 ⚠) | — | [[Abemaciclib (drug)]] 0.05 µM 0.0482× (z -8.5) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 4.83 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0696× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 8.08 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.137× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 7.46 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.107× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 5.61 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0933× (z -8.9) |
| [[A-172 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3258), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC23]] | +0.76 | +0.75 / +0.74 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[DHDH]] | +0.72 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[DALRD3]] | +0.71 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[IFRD1]] | +0.67 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[FAM53C]] | +0.65 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[APC2]] | +0.63 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[DDIT3]] | +0.63 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[CPT1C]] | +0.63 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[MIR9-1HG]] | +0.62 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[AZU1]] | +0.60 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[COQ10B]] | +0.60 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[LDHC]] | +0.60 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[GRAMD2A]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTAR1]] | -0.64 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[RFT1]] | -0.61 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[NHLRC2]] | -0.60 | -0.27 / -0.73 | both halves | 3e-04 |  |
| [[VMA21]] | -0.57 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[MRPL42]] | -0.57 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[IDH3A]] | -0.56 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[IPO9]] | -0.56 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[TMEM209]] | -0.56 | -0.40 / -0.56 | both halves | 4e-05 |  |
| [[TMX1]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[MTHFD1]] | -0.55 | -0.35 / -0.63 | both halves | 1e-04 |  |
| [[SRP9]] | -0.53 | -0.38 / -0.61 | both halves | 6e-05 |  |
| [[RPE]] | -0.53 | -0.44 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFNA2]] | B | EFNA2 activity raises SPSB2's level | lines that do not express EFNA2 (8) vs lines expressing it (42) | 1.34× lower at baseline in the lines without EFNA2 | 0.059 | ⚠ within organs, on part of the lines; also absent: TFR2, USP43, BTG3-AS1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MED26]] | C | SPSB2's natural level weakens MED26's drug response | SPSB2's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.03; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.646). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.2, -25.2); signed map (11.8, 16.0). **Vector** length 50.0, 6.55% of its response variance represented; |z| ≥ 3 in 741 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +1.5 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.1 | +1.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.1 | +1.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.0 | +1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.0 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -3.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.1 | -2.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.0 | -4.2 |
|  | [[Gallic acid (drug)]] 0.05 µM |  | -1.1 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -1.7 |
|  | [[Balsalazide (sodium hydrate) (drug)]] 0.05 µM |  | -0.9 | -1.2 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -2.0 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -0.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | splA/ryanodine receptor domain and SOCS box containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,870,935-6,889,358 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GRCC9, SSB-2 |
| Gene groups (HGNC) | SplA/ryanodine receptor domain and SOCS box containing family |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99619](https://www.uniprot.org/uniprotkb/Q99619) (SPRY domain-containing SOCS box protein 2):

> Substrate recognition component of a SCF-like ECS (Elongin BC-CUL2/5-SOCS-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Negatively regulates nitric oxide (NO) production and limits cellular toxicity in activated macrophages by mediating the ubiquitination and proteasomal degradation of NOS2. Acts as a bridge which links NOS2 with the ECS E3 ubiquitin ligase complex components ELOC and CUL5.

**Summary**, from NCBI Gene [84727](https://www.ncbi.nlm.nih.gov/gene/84727):

> This gene encodes a member of a subfamily of proteins containing a central SPRY (repeats in splA and RyR) domain and a C-terminal suppressor of cytokine signaling (SOCS) box. This protein plays a role in cell signaling. This gene is present in a gene-rich cluster on chromosome 12p13 in the vicinity of the CD4 antigen and triosephosphate isomerase genes. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:29522](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29522) · Entrez [84727](https://www.ncbi.nlm.nih.gov/gene/84727) · UniProt [Q99619](https://www.uniprot.org/uniprotkb/Q99619) · Ensembl [ENSG00000111671](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111671)

## Data

Gene col 3258: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3258); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3258, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3258]; `tensor/DDL_lfc|DDL_z.npy` [3258]; `embed/gene_vectors.npy` [3258]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3258 or target_col == 3258). Every well: [[SPSB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPSB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
