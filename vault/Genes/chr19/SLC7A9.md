---
symbol: "SLC7A9"
type: "gene"
col: 326
ensembl_id: "ENSG00000021488"
name: "solute carrier family 7 member 9"
location: "19q13.11"
module: 39
arm: "+"
pooled_cpm: 2.6
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# SLC7A9

*solute carrier family 7 member 9* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.81× (z +12.5, q 3e-33, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +6.3, q 5e-08, up in 18 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.382× (z -4.2, q 0.016, down in 11 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GARIN1B]] (+0.79, fdr 7e-06), [[USP50]] (+0.75, fdr 7e-06), [[SLC6A13]] (+0.75, fdr 7e-06); moves opposite to [[SLC35A1]] (-0.59, fdr 3e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SPOCK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 326.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.81×** | +12.5 | 3e-33 | 2/2 (HOP62, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.97×** | +9.0 | 5e-17 | 5/15 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.22×** | +9.0 | 6e-17 | 3/4 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.3 | 5e-08 | 18/33 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.3 | 0.002 | 11/46 (PANC-1, NCI-H460, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +3.4 | 0.050 | 3/30 (LoVo, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +3.4 | 0.050 | 7/46 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.09×** | +3.2 | 0.096 | 1/6 (PANC-1) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.47×** | +3.2 | 0.096 | 3/30 (SW480, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.50×** | +3.1 | 0.097 | 2/46 (MIA PaCa-2, SHP-77) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Furosemide (drug)]] 5 µM |  | 1.30× | +3.0 | 0.13 | 2/45 (Hs 766T, HepG2/C3A) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 326.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.382×** | -4.2 | 0.016 | 11/27 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.05 µM |  | **0.601×** | -4.0 | 0.017 | 15/37 (HepG2/C3A, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.628×** | -3.7 | 0.035 | 16/42 (A-172, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | 0.657× | -3.2 | 0.17 | 9/43 (A-427, NCI-H2347, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 326. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 7.31 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0943× (z -8.5) |
| [[A-172 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 326), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GARIN1B]] | +0.79 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[USP50]] | +0.75 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.75 | +0.69 / +0.68 | both halves | 7e-06 | pathway: SLC-mediated transmembrane transport; STRING 421 |
| [[ALDH8A1]] | +0.75 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[DPYS]] | +0.74 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[IMPG2]] | +0.74 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[XG]] | +0.74 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[SH2D4B]] | +0.73 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[GARIN1A]] | +0.73 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[IMPA1P1]] | +0.73 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[LINC02133]] | +0.71 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[QRICH2]] | +0.71 | +0.69 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35A1]] | -0.59 | -0.54 / -0.46 | both halves | 3e-05 | pathway: Disorders of transmembrane transporters |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPOCK2]] | B | SPOCK2 activity raises SLC7A9's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.36× lower at baseline in the lines without SPOCK2 | 0.067 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |
| [[SLC26A4]] | B | SLC26A4 activity raises SLC7A9's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.33× lower at baseline in the lines without SLC26A4 | 0.080 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.758). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.1, -13.4); signed map (18.3, 9.3). **Vector** length 43.1, 4.20% of its response variance represented; |z| ≥ 3 in 1,204 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +6.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +1.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.0 | +1.2 |
| fall | [[Radotinib (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[NG25 (drug)]] 5 µM |  | -1.9 | -4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -0.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.6 | -1.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +0.5 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.2 | -0.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 7 member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:32,830,509-32,869,767 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BAT1; previously CSNU3 |
| Gene groups (HGNC) | Solute carrier family 7 |
| Reactome | 9 pathways, smallest: Basigin interactions; Amino acid transport across the plasma membrane; SLC-mediated transport of amino acids |
| Matched by | ensembl_id |

**Function**, from UniProt [P82251](https://www.uniprot.org/uniprotkb/P82251) (b(0,+)-type amino acid transporter 1):

> Associates with SLC3A1 to form a functional transporter complex that mediates the electrogenic exchange between cationic amino acids and neutral amino acids, with a stoichiometry of 1:1. Has system b(0,+)-like activity with high affinity for extracellular cationic amino acids and L-cystine and lower affinity for intracellular neutral amino acids. Substrate exchange is driven by high concentration of intracellular neutral amino acids and the intracellular reduction of L-cystine to L-cysteine. …

**Summary**, from NCBI Gene [11136](https://www.ncbi.nlm.nih.gov/gene/11136):

> This gene encodes a protein that belongs to a family of light subunits of amino acid transporters. This protein plays a role in the high-affinity and sodium-independent transport of cystine and neutral and dibasic amino acids, and appears to function in the reabsorption of cystine in the kidney tubule. Mutations in this gene cause non-type I cystinuria, a disease that leads to cystine stones in the urinary system due to impaired transport of cystine and dibasic amino acids. Alternate transcript …

**Accessions** — [HGNC:11067](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11067) · Entrez [11136](https://www.ncbi.nlm.nih.gov/gene/11136) · UniProt [P82251](https://www.uniprot.org/uniprotkb/P82251) · Ensembl [ENSG00000021488](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000021488)

## Data

Gene col 326: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 326); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 326, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 326]; `tensor/DDL_lfc|DDL_z.npy` [326]; `embed/gene_vectors.npy` [326]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 326 or target_col == 326). Every well: [[SLC7A9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC7A9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
