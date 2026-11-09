---
symbol: "CAPN12"
type: "gene"
col: 11288
ensembl_id: "ENSG00000182472"
name: "calpain 12"
location: "19q13.2"
module: 53
arm: "+"
pooled_cpm: 10.34
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# CAPN12

*calpain 12* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.15× (z +9.0, q 9e-17, up in 21 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.31× (z +4.5, q 8e-04, up in 17 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.593× (z -6.2, q 3e-07, down in 23 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC88B]] (+0.64, fdr 1e-05), [[PPM1N]] (+0.64, fdr 1e-05), [[GP6]] (+0.63, fdr 7e-06); moves opposite to [[SLC35B4]] (-0.50, fdr 4e-05), [[VPS4A]] (-0.49, fdr 3e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LMTK3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11288.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +9.0 | 9e-17 | 21/31 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +8.0 | 3e-13 | 6/15 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +4.9 | 2e-04 | 8/20 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.5 | 8e-04 | 17/42 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.051 | 7/44 (SHP-77, LoVo, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.096 | 3/46 (J82, NCI-H460, …) | top dose only |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.096 | 6/44 (SW 900, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.2 | 0.096 | 6/40 (AsPC-1, H4, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.29× | +3.0 | 0.14 | 6/35 (A498, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11288.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.593×** | -6.2 | 3e-07 | 23/46 (PANC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.596×** | -5.9 | 1e-06 | 22/43 (NCI-H2030, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.629×** | -5.5 | 7e-06 | 22/45 (H4, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.644×** | -5.2 | 3e-05 | 19/46 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.679×** | -4.4 | 0.001 | 18/37 (HT-29, C32, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.690×** | -4.4 | 0.001 | 15/46 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.700×** | -4.2 | 0.002 | 17/43 (COLO 205, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.759×** | -3.3 | 0.074 | 10/46 (HOP62, SK-MEL-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.755× | -3.2 | 0.10 | 5/47 (SW 1088, NCI-H1573, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.749× | -3.1 | 0.11 | 5/45 (C32, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11288. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 27.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.224× (z -9.1) |
| [[COLO 205 (line)]] | alt | 14.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 8.17 | 0 | 1 | — | [[Proglumide (drug)]] 0.05 µM 0.0746× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 7.14 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0350× (z -13.9) |
| [[PANC-1 (line)]] | alt | 42.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -8.5) |
| [[A-172 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11288), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC88B]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[PPM1N]] | +0.64 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[GP6]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[GGT1]] | +0.62 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[DHDH]] | +0.61 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[CELF5]] | +0.58 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[CASKIN1]] | +0.57 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[CFAP45]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[AMZ1]] | +0.57 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CDKL2]] | +0.57 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[ITGA7]] | +0.57 | +0.41 / +0.59 | both halves | 4e-05 | pathway: Extracellular matrix organization |
| [[TCEA3]] | +0.57 | +0.42 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35B4]] | -0.50 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[VPS4A]] | -0.49 | -0.45 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMTK3]] | B | LMTK3 activity raises CAPN12's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 1.66× lower at baseline in the lines without LMTK3 | 0.018 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[PTPN6]] | B | PTPN6 activity raises CAPN12's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.60× lower at baseline in the lines without PTPN6 | 0.047 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |
| [[FCGBP]] | B | FCGBP activity raises CAPN12's level | lines that do not express FCGBP (20) vs lines expressing it (30) | 1.36× lower at baseline in the lines without FCGBP | 0.054 | ⚠ within organs, on part of the lines; also absent: LCN2, NPNT, RNF183; maybe low, not absent |
| [[SLC26A2]] | C | SLC26A2 activity lowers CAPN12's level | lines that do not express SLC26A2 (4) vs lines expressing it (46) | 1.70× higher at baseline in the lines without SLC26A2 | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MIR4435-2HG, EPB41L2, CEP85L; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.539). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.1, -18.7); signed map (13.0, 15.9). **Vector** length 57.0, 8.13% of its response variance represented; |z| ≥ 3 in 796 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | -0.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.0 | -5.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -6.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.9 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -5.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | calpain 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,730,187-38,769,904 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | EF-hand domain containing; Calpains |
| Reactome | 2 pathways, smallest: Degradation of the extracellular matrix; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZSI9](https://www.uniprot.org/uniprotkb/Q6ZSI9) (Calpain-12):

> Calcium-regulated non-lysosomal thiol-protease.

**Summary**, from NCBI Gene [147968](https://www.ncbi.nlm.nih.gov/gene/147968):

> The calpains, calcium-activated neutral proteases, are nonlysosomal, intracellular cysteine proteases. The mammalian calpains include ubiquitous, stomach-specific, and muscle-specific proteins. The ubiquitous enzymes consist of heterodimers with distinct large, catalytic subunits associated with a common small, regulatory subunit. This gene encodes a member of the calpain large subunit family. [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:13249](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13249) · Entrez [147968](https://www.ncbi.nlm.nih.gov/gene/147968) · UniProt [Q6ZSI9](https://www.uniprot.org/uniprotkb/Q6ZSI9) · Ensembl [ENSG00000182472](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182472)

## Data

Gene col 11288: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11288); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11288, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11288]; `tensor/DDL_lfc|DDL_z.npy` [11288]; `embed/gene_vectors.npy` [11288]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11288 or target_col == 11288). Every well: [[CAPN12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAPN12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
