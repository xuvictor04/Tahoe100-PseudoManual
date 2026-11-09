---
symbol: "RFT1"
type: "gene"
col: 8814
ensembl_id: "ENSG00000163933"
name: "RFT1 glycolipid translocator homolog"
location: "3p21.1"
module: 18
arm: "+"
pooled_cpm: 10.04
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 6
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# RFT1

*RFT1 glycolipid translocator homolog* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.30× (z +4.6, q 0.003, up in 15 of 48 measured lines) ⚠ cell-cycle shift, explains ~61% of this change.
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.606× (z -8.6, q 3e-15, down in 29 of 46 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.728× (z -5.5, q 8e-06, down in 22 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POFUT1]] (+0.76, fdr 7e-06), [[TMEM209]] (+0.74, fdr 7e-06), [[TIGD1]] (+0.72, fdr 1e-05); moves opposite to [[SPSB2]] (-0.61, fdr 1e-05), [[ANKHD1]] (-0.60, fdr 2e-05), [[ZMYM5]] (-0.59, fdr 9e-06).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SMARCA2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8814.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.30×** | +4.6 | 0.003 | 15/48 (NCI-H1573, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | 1.35× | +3.5 | 0.13 | 14/37 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[Folic acid (drug)]] 5 µM |  | 1.21× | +3.2 | 0.22 | 10/48 (SW1417, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.31× | +3.1 | 0.25 | 3/17 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8814.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.606×** | -8.6 | 3e-15 | 29/46 (SNU-423, HEC-1-A, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.570×** | -6.6 | 1e-08 | 31/46 (PANC-1, SK-MEL-2, …) | rises with dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.728×** | -5.5 | 8e-06 | 22/43 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.687×** | -4.4 | 0.002 | 18/38 (SNU-423, J82, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.509×** | -4.3 | 0.002 | 16/46 (LS 180, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **0.748×** | -3.5 | 0.037 | 12/47 (SNU-423, A-172, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.704× | -3.1 | 0.18 | 11/43 (HS-578T, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8814. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 8.52 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -11.2) ⚠ cell-cycle shift, explains ~51% of this change |
| [[C32 (line)]] | wt | 8.35 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -10.1) ⚠ cell-cycle shift, explains ~51% of this change |
| [[MIA PaCa-2 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.203× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8814), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POFUT1]] | +0.76 | +0.81 / +0.76 | both halves | 7e-06 |  |
| [[TMEM209]] | +0.74 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[TIGD1]] | +0.72 | +0.55 / +0.80 | both halves | 1e-05 |  |
| [[CAD]] | +0.71 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[RPE]] | +0.71 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[METTL3]] | +0.70 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[ZFP62]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[DTD2]] | +0.68 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[ADAT2]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[EEF1E1]] | +0.68 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[MTG1]] | +0.66 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[ZC3HAV1L]] | +0.66 | +0.60 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPSB2]] | -0.61 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[ANKHD1]] | -0.60 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[ZMYM5]] | -0.59 | -0.57 / -0.60 | both halves | 9e-06 |  |
| [[AVIL]] | -0.59 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[TLE4]] | -0.59 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[ANKRD12]] | -0.58 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[ARIH1]] | -0.58 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[ARID4A]] | -0.57 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[ZSWIM6]] | -0.57 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[NBPF10]] | -0.56 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[ING2]] | -0.56 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[SHOC2]] | -0.56 | -0.45 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMARCA2]] | B | SMARCA2 activity lowers RFT1's level | lines that do not express SMARCA2 (6) vs lines expressing it (44) | 1.35× higher at baseline in the lines without SMARCA2 | 0.044 | ⚠ within organs, on part of the lines; also absent: CEMIP2, S100A13, PYROXD2 |
| [[TSEN2]] | C | TSEN2 activity raises RFT1's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 1.73× lower at baseline in the lines without TSEN2 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.595). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-11.9, -31.3); signed map (-3.1, -51.8). **Vector** length 70.6, 11.8% of its response variance represented; |z| ≥ 3 in 830 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.50 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | +4.6 | +3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +3.8 | +4.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.6 | -1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -4.6 | -8.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.1 | -6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -5.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.9 | -3.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | RFT1 glycolipid translocator homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:53,088,483-53,130,453 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDG1N, SLC76A1 |
| Gene groups (HGNC) | Solute carrier family 76 |
| Reactome | 5 pathways, smallest: Diseases associated with N-glycosylation of proteins; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein; Diseases of glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AA3](https://www.uniprot.org/uniprotkb/Q96AA3) (Man(5)GlcNAc(2)-PP-dolichol translocation protein RFT1):

> Intramembrane glycolipid transporter that operates in the biosynthetic pathway of dolichol-linked oligosaccharides, the glycan precursors employed in protein asparagine (N)-glycosylation. The sequential addition of sugars to dolichol pyrophosphate produces dolichol-linked oligosaccharides containing fourteen sugars, including two GlcNAcs, nine mannoses and three glucoses. Once assembled, the oligosaccharide is transferred from the lipid to nascent proteins by oligosaccharyltransferases. The …

**Summary**, from NCBI Gene [91869](https://www.ncbi.nlm.nih.gov/gene/91869):

> This gene encodes an enzyme which catalyzes the translocation of the Man(5)GlcNAc (2)-PP-Dol intermediate from the cytoplasmic to the luminal side of the endoplasmic reticulum membrane in the pathway for the N-glycosylation of proteins. Mutations in this gene are associated with congenital disorder of glycosylation type In.[provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:30220](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30220) · Entrez [91869](https://www.ncbi.nlm.nih.gov/gene/91869) · UniProt [Q96AA3](https://www.uniprot.org/uniprotkb/Q96AA3) · Ensembl [ENSG00000163933](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163933)

## Data

Gene col 8814: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8814); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8814, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8814]; `tensor/DDL_lfc|DDL_z.npy` [8814]; `embed/gene_vectors.npy` [8814]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8814 or target_col == 8814). Every well: [[RFT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
