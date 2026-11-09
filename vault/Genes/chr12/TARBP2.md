---
symbol: "TARBP2"
type: "gene"
col: 6316
ensembl_id: "ENSG00000139546"
name: "TARBP2 subunit of RISC loading complex"
location: "12q13.13"
module: 153
arm: "+"
pooled_cpm: 4.33
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# TARBP2

*TARBP2 subunit of RISC loading complex* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.64× (z +9.7, q 2e-19, up in 21 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.706× (z -4.8, q 7e-04, down in 18 of 46 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POMK]] (+0.64, fdr 1e-05), [[MRPL9]] (+0.64, fdr 1e-05), [[POLR2M]] (+0.62, fdr 8e-05); moves opposite to [[SH3BGRL3]] (-0.54, fdr 9e-05), [[AMN1]] (-0.53, fdr 3e-05), [[CHCHD2]] (-0.52, fdr 4e-05).
> It is in [[Module 153]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6316.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +9.7 | 2e-19 | 21/40 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.87×** | +8.6 | 1e-15 | 15/26 (NCI-H1792, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +8.1 | 1e-13 | 14/25 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +7.8 | 7e-13 | 1/5 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +6.5 | 9e-09 | 19/39 (NCI-H460, SW48, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.6 | 2e-06 | 9/26 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +5.3 | 8e-06 | 3/8 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +4.4 | 6e-04 | 5/46 (NCI-H1792, HOP62, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.007 | 9/46 (A-427, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.3 | 0.049 | 1/11 (A498) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 1.17× | +3.1 | 0.12 | 1/45 (Hs 766T) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6316.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.706×** | -4.8 | 7e-04 | 18/46 (HS-578T, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.743×** | -4.1 | 0.011 | 9/39 (HCT15, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.05 µM |  | **0.759×** | -3.8 | 0.024 | 7/43 (RKO, LOX-IMVI, …) | inconsistent across doses |  |
| [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | 0.840× | -3.4 | 0.086 | 9/45 (MIA PaCa-2, A549, …) | top dose only |  |
| [[Ivermectin (drug)]] 0.05 µM |  | 0.796× | -3.2 | 0.18 | 8/46 (SW1417, HCT15, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.802× | -3.1 | 0.20 | 11/37 (NCI-H460, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6316. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 3.36 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0575× (z -10.1) |
| [[A549 (line)]] | wt | 3.54 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0722× (z -9.4) |
| [[J82 (line)]] | alt | 3.03 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0687× (z -9.6) |
| [[LoVo (line)]] | wt | 5.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +12.6) | — |
| [[LOX-IMVI (line)]] | wt | 4.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +14.1) | — |
| [[NCI-H460 (line)]] | wt | 3.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +10.0) | — |
| [[A-172 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6316), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POMK]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[MRPL9]] | +0.64 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[POLR2M]] | +0.62 | +0.62 / +0.37 | both halves | 8e-05 |  |
| [[ACTR8]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[C17orf75]] | +0.58 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[RAE1]] | +0.58 | +0.49 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_DNA_REPAIR |
| [[PATZ1]] | +0.57 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[STRN4]] | +0.56 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[ATP13A1]] | +0.55 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[FIZ1]] | +0.55 | +0.61 / +0.23 | both halves | 5e-04 |  |
| [[ZNF362]] | +0.55 | +0.53 / +0.35 | both halves | 1e-04 |  |
| [[FECH]] | +0.55 | +0.58 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3BGRL3]] | -0.54 | -0.54 / -0.37 | both halves | 9e-05 |  |
| [[AMN1]] | -0.53 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[CHCHD2]] | -0.52 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[STK4]] | -0.52 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[BAIAP2L1]] | -0.51 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[MYL12B]] | -0.51 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[PIBF1]] | -0.50 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[RPS21]] | -0.49 | -0.53 / -0.26 | both halves | 4e-04 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[PI4KA]] | -0.49 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[SH3GL3]] | -0.49 | -0.48 / -0.24 | both halves | 4e-04 |  |
| [[COX6A1]] | -0.48 | -0.48 / -0.23 | both halves | 5e-04 |  |
| [[PPP1R14B]] | -0.47 | -0.54 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.583). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.0, 5.2); signed map (6.0, -32.0). **Vector** length 42.8, 4.18% of its response variance represented; |z| ≥ 3 in 964 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +9.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +5.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.5 | +8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +7.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.3 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +4.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.2 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.0 | +1.8 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -2.4 | -4.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -4.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.0 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -0.9 | +0.3 |
|  | [[Ciclopirox (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Gallic acid (hydrate) (drug)]] 5 µM |  | -0.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | TARBP2 subunit of RISC loading complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,500,921-53,506,431 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Trbp |
| Gene groups (HGNC) | RISC loading complex subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 7 pathways, smallest: Small interfering RNA (siRNA) biogenesis; MicroRNA (miRNA) biogenesis; Gene Silencing by RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15633](https://www.uniprot.org/uniprotkb/Q15633) (RISC-loading complex subunit TARBP2):

> Required for formation of the RNA induced silencing complex (RISC). Component of the RISC loading complex (RLC), also known as the micro-RNA (miRNA) loading complex (miRLC), which is composed of DICER1, AGO2 and TARBP2. Within the RLC/miRLC, DICER1 and TARBP2 are required to process precursor miRNAs (pre-miRNAs) to mature miRNAs and then load them onto AGO2. AGO2 bound to the mature miRNA constitutes the minimal RISC and may subsequently dissociate from DICER1 and TARBP2. May also play a role …

**Summary**, from NCBI Gene [6895](https://www.ncbi.nlm.nih.gov/gene/6895):

> HIV-1, the causative agent of acquired immunodeficiency syndrome (AIDS), contains an RNA genome that produces a chromosomally integrated DNA during the replicative cycle. Activation of HIV-1 gene expression by the transactivator Tat is dependent on an RNA regulatory element (TAR) located downstream of the transcription initiation site. The protein encoded by this gene binds between the bulge and the loop of the HIV-1 TAR RNA regulatory element and activates HIV-1 gene expression in synergy with …

**Accessions** — [HGNC:11569](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11569) · Entrez [6895](https://www.ncbi.nlm.nih.gov/gene/6895) · UniProt [Q15633](https://www.uniprot.org/uniprotkb/Q15633) · Ensembl [ENSG00000139546](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139546)

## Data

Gene col 6316: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6316); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6316, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6316]; `tensor/DDL_lfc|DDL_z.npy` [6316]; `embed/gene_vectors.npy` [6316]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6316 or target_col == 6316). Every well: [[TARBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TARBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
