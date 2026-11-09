---
symbol: "SLC3A1"
type: "gene"
col: 6121
ensembl_id: "ENSG00000138079"
name: "solute carrier family 3 member 1"
location: "2p21"
module: 21
arm: "+"
pooled_cpm: 3.69
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SLC3A1

*solute carrier family 3 member 1* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.55× (z +14.7, q 0e+00, up in 31 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Vismodegib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0719×); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (NCI-H2347 0.0750×); [[Delamanid (drug)]] 0.5 µM in 1 line (SW 900 0.0671×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHMP3-AS1]] (+0.86, fdr 7e-06), [[SLC23A1]] (+0.82, fdr 7e-06), [[ZRANB2-AS1]] (+0.82, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AMBP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6121.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.55×** | +14.7 | 0e+00 | 31/38 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.66×** | +10.9 | 5e-25 | 14/22 (LOX-IMVI, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +8.0 | 2e-13 | 5/6 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.88×** | +7.0 | 4e-10 | 9/20 (HEC-1-A, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +6.6 | 4e-09 | 15/36 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +5.8 | 7e-07 | 2/7 (A498, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +4.8 | 1e-04 | 14/44 (NCI-H23, RKO, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.5 | 6e-04 | 10/37 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.49×** | +4.4 | 6e-04 | 6/45 (J82, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +4.4 | 6e-04 | 10/36 (NCI-H2347, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +4.2 | 0.002 | 12/45 (COLO 205, NCI-H2030, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.053 | 2/39 (PANC-1, C32) | top dose only |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.2 | 0.062 | 7/43 (A-172, KATO III, …) | top dose only |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.2 | 0.062 | 4/36 (HCT15, SK-MEL-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.073 | 4/34 (LOX-IMVI, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.093 | 7/44 (Hs 766T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.096 | 4/41 (A498, SW480, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6121.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Vismodegib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0719×); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (NCI-H2347 0.0750×); [[Delamanid (drug)]] 0.5 µM in 1 line (SW 900 0.0671×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.884× | -4.6 | 0.002 | 17/48 (RPMI-7951, SW480, …) | inconsistent across doses |  |
| [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM |  | 0.736× | -3.0 | 0.66 | 13/40 (HS-578T, Hs 766T, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6121. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 2.34 | 0 | 2 | — | [[Vismodegib (drug)]] 0.05 µM 0.0719× (z -9.4) |
| [[A498 (line)]] | wt | 2.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.47× (z +10.8) | — |
| [[SW 900 (line)]] | alt | 4.27 | 0 | 1 | — | [[Delamanid (drug)]] 0.5 µM 0.0671× (z -8.5) |
| [[A-172 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6121), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP3-AS1]] | +0.86 | +0.76 / +0.81 | both halves | 7e-06 |  |
| [[SLC23A1]] | +0.82 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.82 | +0.78 / +0.77 | both halves | 7e-06 |  |
| [[PP2D1]] | +0.81 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[FLJ40194]] | +0.80 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[HRG-AS1]] | +0.80 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[TOMM20L-DT]] | +0.80 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.80 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[DLEU7]] | +0.78 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[CTDSPL2-DT]] | +0.78 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[LANCL1-AS1]] | +0.77 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.77 | +0.70 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AMBP]] | B | AMBP activity raises SLC3A1's level | lines that do not express AMBP (41) vs lines expressing it (9) | 1.18× lower at baseline in the lines without AMBP | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2 |
| [[LINC02932]] | B | LINC02932 activity raises SLC3A1's level | lines that do not express LINC02932 (5) vs lines expressing it (45) | 1.28× lower at baseline in the lines without LINC02932 | 0.060 | ⚠ within organs, on part of the lines; also absent: RBFOX1, DNAH6, ESRRB; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.847). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.4, 27.2); signed map (33.1, 5.1). **Vector** length 45.5, 5.09% of its response variance represented; |z| ≥ 3 in 825 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +14.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +4.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +1.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | -0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 3 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:44,275,458-44,321,494 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CSNU1, D2H, RBAT, ATR1, NBAT |
| Gene groups (HGNC) | Solute carrier family 3 |
| Reactome | 6 pathways, smallest: Amino acid transport across the plasma membrane; SLC-mediated transport of amino acids; SLC transporter disorders |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07837](https://www.uniprot.org/uniprotkb/Q07837) (Amino acid transporter heavy chain SLC3A1):

> Acts as a chaperone that facilitates biogenesis and trafficking of functional transporter heteromers to the plasma membrane (By similarity). Associates with SLC7A9 to form a functional transporter complex that mediates the electrogenic exchange between cationic amino acids and neutral amino acids, with a stoichiometry of 1:1. SLC7A9-SLC3A1 transporter has system b(0,+)-like activity with high affinity for extracellular cationic amino acids and L-cystine and lower affinity for intracellular …

**Summary**, from NCBI Gene [6519](https://www.ncbi.nlm.nih.gov/gene/6519):

> This gene encodes a type II membrane glycoprotein which is one of the components of the renal amino acid transporter which transports neutral and basic amino acids in the renal tubule and intestinal tract. Mutations and deletions in this gene are associated with cystinuria. Alternatively spliced transcript variants have been described, but their biological validity has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11025](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11025) · Entrez [6519](https://www.ncbi.nlm.nih.gov/gene/6519) · UniProt [Q07837](https://www.uniprot.org/uniprotkb/Q07837) · Ensembl [ENSG00000138079](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138079)

## Data

Gene col 6121: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6121); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6121, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6121]; `tensor/DDL_lfc|DDL_z.npy` [6121]; `embed/gene_vectors.npy` [6121]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6121 or target_col == 6121). Every well: [[SLC3A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC3A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
