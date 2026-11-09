---
symbol: "BARX1"
type: "gene"
col: 5231
ensembl_id: "ENSG00000131668"
name: "BARX homeobox 1"
location: "9q22.32"
module: 19
arm: "+"
pooled_cpm: 2.34
n_lines_expressing: 20
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# BARX1

*BARX homeobox 1* — 9q22.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 8.21× (z +10.9, q 6e-25, up in 3 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.93× (z +5.0, q 5e-05, up in 3 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Erlotinib (drug)]] 0.05 µM: 0.456× (z -3.9, q 0.038, down in 5 of 16 measured lines).
> Its strongest partners by |cos| (80 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCKAP5-AS2]] (+0.63, fdr 1e-05), [[C3orf18]] (+0.58, fdr 1e-04), [[NEFL]] (+0.57, fdr 3e-05); moves opposite to [[ZNF529]] (-0.42, fdr 3e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[CIB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5231.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.21×** | +10.9 | 6e-25 | 3/3 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.51×** | +8.1 | 1e-13 | 3/7 (PANC-1, NCI-H661, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.07×** | +7.0 | 5e-10 | 1/4 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.72×** | +5.4 | 1e-05 | 7/9 (A-427, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.55×** | +5.0 | 5e-05 | 3/12 (A-427, NCI-H661, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.93×** | +5.0 | 5e-05 | 3/16 (NCI-H2347, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.61×** | +5.0 | 5e-05 | 1/10 (NCI-H661) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.43×** | +5.0 | 5e-05 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | **1.79×** | +4.4 | 7e-04 | 2/14 (AN3 CA, NCI-H23) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +4.3 | 9e-04 | 3/12 (NCI-H2347, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.78×** | +3.7 | 0.009 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +3.7 | 0.011 | 0/12 | top dose only | cell-cycle shift (explains ~6% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.98×** | +3.5 | 0.018 | 1/10 (NCI-H2030) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.89×** | +3.4 | 0.026 | 0/8 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.87×** | +3.4 | 0.028 | 2/9 (A-427, NCI-H23) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.58×** | +3.2 | 0.051 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.77×** | +3.1 | 0.063 | 3/12 (AN3 CA, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.75×** | +3.0 | 0.078 | 0/11 | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5231.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 0.05 µM |  | **0.456×** | -3.9 | 0.038 | 5/16 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.480×** | -3.8 | 0.038 | 8/15 (A549, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | **0.484×** | -3.6 | 0.052 | 4/16 (C-33 A, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5231. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 4.78 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0303× (z -16.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Rifaximin (drug)]] 5 µM 0.0597× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 4.94 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0721× (z -13.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0329× (z -12.4) |
| [[PANC-1 (line)]] | alt | 12.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -11.9) |
| [[SHP-77 (line)]] | alt | 7.47 | 0 | 2 | — | [[Vilanterol (drug)]] 0.05 µM 0.0747× (z -9.1) |
| [[HOP62 (line)]] | alt | 4.67 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 1.54 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.244 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.124 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.153 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.139 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.183 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.135 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.163 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.162 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.140 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.142 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.131 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.178 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.216 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.818 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.151 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.187 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.176 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.151 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.113 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.998 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.122 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.149 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.666 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.138 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.189 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.138 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.165 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.208 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5231), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 20 of them with an alert (⚠; 20 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCKAP5-AS2]] | +0.63 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[C3orf18]] | +0.58 | +0.60 / +0.33 | both halves | 1e-04 |  |
| [[NEFL]] | +0.57 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[SEC14L4]] | +0.56 | +0.53 / +0.37 | both halves | 9e-05 | **novel candidate** |
| [[TBX1]] | +0.55 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[BOLA3-DT]] | +0.55 | +0.61 / +0.29 | both halves | 2e-04 |  |
| [[EYA2]] | +0.55 | +0.62 / +0.30 | both halves | 2e-04 |  |
| [[TWIST2]] | +0.54 | +0.59 / +0.30 | both halves | 2e-04 |  |
| [[SPDYE10]] | +0.53 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[BASP1-AS1]] | +0.52 | +0.68 / +0.25 | both halves | 4e-04 |  |
| [[PRAME]] | +0.51 | +0.49 / +0.38 | both halves | 6e-05 |  |
| [[NEXMIF]] | +0.49 | +0.50 / +0.23 | both halves | 5e-04 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF529]] | -0.42 | -0.29 / -0.48 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CIB2]] | B | BARX1 activity raises CIB2's level | lines that do not express BARX1 (30) vs lines expressing it (20) | 2.29× lower at baseline in the lines without BARX1 | 0.065 | ⚠ within organs, on part of the lines; also absent: INA, LIN28B, NEXMIF |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.469). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.8, 40.6); signed map (22.5, 26.0). **Vector** length 28.1, 5.53% of its response variance represented; |z| ≥ 3 in 320 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +1.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.5 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.4 | +8.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.3 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.7 | +1.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.7 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -1.8 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.3 | -1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -0.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.8 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -2.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | BARX homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.32 — chr9:93,951,627-93,955,355 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | NKL subclass homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBU1](https://www.uniprot.org/uniprotkb/Q9HBU1) (Homeobox protein BarH-like 1):

> Transcription factor, which is involved in craniofacial development, in odontogenesis and in stomach organogenesis. May have a role in the differentiation of molars from incisors. Plays a role in suppressing endodermal Wnt activity (By similarity). Binds to a regulatory module of the NCAM promoter.

**Summary**, from NCBI Gene [56033](https://www.ncbi.nlm.nih.gov/gene/56033):

> This gene encodes a member of the Bar subclass of homeobox transcription factors. Studies of the mouse and chick homolog suggest the encoded protein may play a role in developing teeth and craniofacial mesenchyme of neural crest origin. The protein may also be associated with differentiation of stomach epithelia. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:955](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:955) · Entrez [56033](https://www.ncbi.nlm.nih.gov/gene/56033) · UniProt [Q9HBU1](https://www.uniprot.org/uniprotkb/Q9HBU1) · Ensembl [ENSG00000131668](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131668)

## Data

Gene col 5231: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5231); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5231, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5231]; `tensor/DDL_lfc|DDL_z.npy` [5231]; `embed/gene_vectors.npy` [5231]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5231 or target_col == 5231). Every well: [[BARX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BARX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
