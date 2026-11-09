---
symbol: "HPX"
type: "gene"
col: 3119
ensembl_id: "ENSG00000110169"
name: "hemopexin"
location: "11p15.4"
module: 47
arm: "+"
pooled_cpm: 2.27
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# HPX

*hemopexin* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.38× (z +11.3, q 5e-27, up in 24 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Rosiglitazone (drug)]] 5 µM in 1 line (HEC-1-A 0.109×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VWCE]] (+0.83, fdr 7e-06), [[TRIM72]] (+0.81, fdr 7e-06), [[XG]] (+0.81, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3119.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.38×** | +11.3 | 5e-27 | 24/30 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **4.26×** | +9.6 | 3e-19 | 40/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.90×** | +9.0 | 6e-17 | 28/39 (LoVo, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.00×** | +8.8 | 2e-16 | 1/2 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.55×** | +8.7 | 3e-16 | 18/27 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **3.24×** | +7.1 | 1e-10 | 31/41 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.16×** | +7.0 | 2e-10 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.89×** | +7.0 | 2e-10 | 33/41 (AsPC-1, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.68×** | +6.2 | 3e-08 | 10/24 (A498, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.50×** | +6.0 | 1e-07 | 16/27 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **2.24×** | +5.1 | 2e-05 | 5/12 (NCI-H1573, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.13×** | +4.9 | 4e-05 | 17/43 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +4.8 | 8e-05 | 13/43 (LS 180, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.85×** | +4.0 | 0.002 | 13/43 (A498, SW48, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.77×** | +3.7 | 0.007 | 0/11 | all doses, stronger at high dose | composition shift |
| [[Naproxen (drug)]] 0.05 µM |  | **1.73×** | +3.3 | 0.032 | 5/23 (LoVo, A498, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.034 | 4/43 (A-172, A549, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.59×** | +3.0 | 0.079 | 3/44 (A498, HOP62, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.57×** | +2.9 | 0.094 | 6/43 (HCT15, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3119.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Rosiglitazone (drug)]] 5 µM in 1 line (HEC-1-A 0.109×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM |  | 0.592× | -3.5 | 0.14 | 10/42 (A549, Panc 03.27, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.370× | -3.5 | 0.14 | 11/21 (A549, A498, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.69 per unit of S-phase module lfc, -0.62 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3119. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 4.95 | 0 | 1 | — | [[Rosiglitazone (drug)]] 5 µM 0.109× (z -8.9) |
| [[LoVo (line)]] | wt | 4.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.71× (z +10.1) | — |
| [[A-172 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.640 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.867 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.958 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3119), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VWCE]] | +0.83 | +0.78 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[TRIM72]] | +0.81 | +0.86 / +0.76 | both halves | 7e-06 |  |
| [[XG]] | +0.81 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[FNDC7]] | +0.79 | +0.83 / +0.77 | both halves | 7e-06 |  |
| [[RFPL3S]] | +0.79 | +0.82 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[CPNE9]] | +0.78 | +0.81 / +0.73 | both halves | 7e-06 |  |
| [[COL20A1]] | +0.78 | +0.77 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[MYO15A]] | +0.78 | +0.77 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[IMPA1P1]] | +0.78 | +0.83 / +0.76 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.77 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[PILRA]] | +0.77 | +0.82 / +0.74 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HPX's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[C21orf91-OT1]] | B | C21orf91-OT1 activity raises HPX's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 1.50× lower at baseline in the lines without C21orf91-OT1 | 0.040 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[SLC26A4]] | B | SLC26A4 activity raises HPX's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.46× lower at baseline in the lines without SLC26A4 | 0.046 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[TP53]] | C | TP53 activity strengthens HPX's drug response | recorded loss-of-function mutation of TP53 in 27 lines vs 17 not recorded | the TP53-altered lines respond 0.80× as strongly (z diff +0.68); strongest at Doxorubicin (hydrochloride) 5 µM: 1.64x vs 9.61x (z diff +4.2) | 0.907 over the table, 0.083 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.842). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.4, -16.1); signed map (16.2, 12.4). **Vector** length 61.6, 9.24% of its response variance represented; |z| ≥ 3 in 1,232 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.8 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +3.5 | +3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +11.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +4.8 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.8 | -3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.3 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | hemopexin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:6,431,049-6,442,617 (-) |
| Ensembl biotype | protein_coding |
| Reactome | 3 pathways, smallest: Scavenging of heme from plasma; Binding and Uptake of Ligands by Scavenger Receptors; Vesicle-mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P02790](https://www.uniprot.org/uniprotkb/P02790) (Hemopexin):

> Binds heme and transports it to the liver for breakdown and iron recovery, after which the free hemopexin returns to the circulation.

**Summary**, from NCBI Gene [3263](https://www.ncbi.nlm.nih.gov/gene/3263):

> This gene encodes a plasma glycoprotein that binds heme with high affinity. The encoded protein is an acute phase protein that transports heme from the plasma to the liver and may be involved in protecting cells from oxidative stress. [provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:5171](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5171) · Entrez [3263](https://www.ncbi.nlm.nih.gov/gene/3263) · UniProt [P02790](https://www.uniprot.org/uniprotkb/P02790) · Ensembl [ENSG00000110169](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110169)

## Data

Gene col 3119: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3119); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3119, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3119]; `tensor/DDL_lfc|DDL_z.npy` [3119]; `embed/gene_vectors.npy` [3119]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3119 or target_col == 3119). Every well: [[HPX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HPX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
