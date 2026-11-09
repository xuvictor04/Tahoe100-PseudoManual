---
symbol: "COPS9"
type: "gene"
col: 10255
ensembl_id: "ENSG00000172428"
name: "COP9 signalosome subunit 9"
location: "2q37.3"
module: 48
arm: "+"
pooled_cpm: 13.72
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# COPS9

*COP9 signalosome subunit 9* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.90× (z +7.8, q 5e-12, up in 34 of 34 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +4.7, q 3e-04, up in 33 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNLZ]] (+0.76, fdr 7e-06), [[MIF]] (+0.75, fdr 7e-06), [[UQCR11]] (+0.75, fdr 7e-06); moves opposite to [[BACE1-AS]] (-0.66, fdr 1e-05), [[SRSF3]] (-0.63, fdr 1e-05), [[PRELID3B]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10255.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **3.90×** | +7.8 | 5e-12 | 34/34 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **3.36×** | +7.2 | 1e-10 | 24/28 (A-172, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.12×** | +6.8 | 2e-09 | 40/40 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.88×** | +6.6 | 4e-09 | 41/46 (COLO 205, HOP62, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.29×** | +4.8 | 2e-04 | 28/32 (SNU-423, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +4.7 | 3e-04 | 33/45 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **2.07×** | +4.6 | 4e-04 | 35/43 (HOP62, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.88×** | +4.0 | 0.005 | 27/47 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.87×** | +3.9 | 0.006 | 28/48 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.008 | 25/48 (A-172, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10255.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 5 µM |  | 0.375× | -3.1 | 0.68 | 26/48 (C-33 A, A-172, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10255. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10255), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 17 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNLZ]] | +0.76 | +0.63 / +0.77 | both halves | 7e-06 |  |
| [[MIF]] | +0.75 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[UQCR11]] | +0.75 | +0.74 / +0.75 | both halves | 7e-06 | STRING 441 |
| [[C1orf122]] | +0.74 | +0.61 / +0.79 | both halves | 7e-06 |  |
| [[NDUFA13]] ⚠ | +0.74 | +0.71 / +0.75 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MG]] | +0.73 | +0.75 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[NDUFB11]] ⚠ | +0.72 | +0.63 / +0.74 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[HIGD2A]] | +0.72 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[MRPL41]] ⚠ | +0.72 | +0.70 / +0.84 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[C19orf53]] | +0.72 | +0.60 / +0.82 | both halves | 7e-06 | STRING 538 |
| [[UBL5]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 | STRING 462 |
| [[ROMO1]] | +0.70 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[NDUFS8]] | +0.70 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[NDUFA3]] | +0.70 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[NDUFB1]] | +0.70 | +0.58 / +0.76 | both halves | 8e-06 | STRING 468 |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BACE1-AS]] | -0.66 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[SRSF3]] | -0.63 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[PRELID3B]] | -0.62 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[SF3B1]] | -0.59 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[PDAP1]] | -0.58 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[AZIN1]] | -0.57 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[NONO]] | -0.57 | -0.33 / -0.75 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.761). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-47.3, -21.6); signed map (-36.2, 9.3). **Vector** length 58.3, 14.4% of its response variance represented; |z| ≥ 3 in 524 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.60 to 31); *Respiratory electron transport* (reactome, mean cos +0.60 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.59 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +4.3 | +6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +4.1 | +4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +3.2 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.3 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.6 | +0.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | -2.3 | +4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -1.7 | +7.2 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.3 | -2.3 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.1 | -0.8 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | COP9 signalosome subunit 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:240,126,563-240,136,807 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CSNAP; previously MYEOV2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXC6](https://www.uniprot.org/uniprotkb/Q8WXC6) (COP9 signalosome complex subunit 9):

> [Isoform 1]: Component of the COP9 signalosome (CSN), a master regulator of the ubiquitin conjugation pathway. CSN mediates the deneddylation of the cullin subunits of all cullin-RING ligases. By reversing the activating neddylation on the cullin-RING ligase, the COP9 signalosome restores the ligase to its inactive state and resets it for substrate recognition. CSN is also involved in phosphorylation of p53/TP53, c-jun/JUN, IkappaBalpha/NFKBIA, ITPK1 and IRF8/ICSBP, possibly via its association …

**Summary**, from NCBI Gene [150678](https://www.ncbi.nlm.nih.gov/gene/150678):

> Involved in several processes, including cellular response to UV; negative regulation of protein localization to nucleolus; and negative regulation of protein neddylation. Located in chromatin; cytoplasm; and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21314](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21314) · Entrez [150678](https://www.ncbi.nlm.nih.gov/gene/150678) · UniProt [Q8WXC6](https://www.uniprot.org/uniprotkb/Q8WXC6) · Ensembl [ENSG00000172428](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172428)

## Data

Gene col 10255: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10255); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10255, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10255]; `tensor/DDL_lfc|DDL_z.npy` [10255]; `embed/gene_vectors.npy` [10255]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10255 or target_col == 10255). Every well: [[COPS9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPS9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
