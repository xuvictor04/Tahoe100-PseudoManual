---
symbol: "ROMO1"
type: "gene"
col: 4705
ensembl_id: "ENSG00000125995"
name: "reactive oxygen species modulator 1"
location: "20q11.22"
module: 48
arm: "+"
pooled_cpm: 54.16
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# ROMO1

*reactive oxygen species modulator 1* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.17× (z +5.8, q 4e-06, up in 35 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A549 8.00×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.566× (z -4.2, q 0.016, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UQCRQ]] (+0.92, fdr 7e-06, ⚠ UQCRQ in the vector space only through flagged drug-doses), [[ATP5MK]] (+0.88, fdr 7e-06), [[COX6B1]] (+0.86, fdr 7e-06), [[ATP5PD]] (+0.85, fdr 7e-06); moves opposite to [[ZNF460]] (-0.68, fdr 1e-05), [[NRAS]] (-0.67, fdr 3e-05), [[U2AF2]] (-0.65, fdr 6e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4705.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A549 8.00×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **3.17×** | +5.8 | 4e-06 | 35/40 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **4.22×** | +5.6 | 5e-06 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **2.10×** | +3.9 | 0.019 | 42/48 (CFPAC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **2.06×** | +3.7 | 0.019 | 37/47 (PANC-1, NCI-H1573, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +3.7 | 0.019 | 37/47 (C32, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.17×** | +3.7 | 0.019 | 35/43 (SNU-423, A-172, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4705.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.566×** | -4.2 | 0.016 | 36/47 (RPMI-7951, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.248×** | -3.8 | 0.043 | 45/47 (H4, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.282× | -3.4 | 0.11 | 44/48 (AsPC-1, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.67 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4705. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 32.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.00× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[A-172 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 83.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 65.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 82.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 47.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4705), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCRQ]] ⚠ | +0.92 | +0.85 / +0.93 | both halves | 7e-06 | STRING 755; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MK]] | +0.88 | +0.82 / +0.87 | both halves | 7e-06 | STRING 457 |
| [[COX6B1]] | +0.86 | +0.78 / +0.88 | both halves | 7e-06 | STRING 682 |
| [[ATP5PD]] | +0.85 | +0.73 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[C4orf48]] | +0.84 | +0.72 / +0.83 | both halves | 7e-06 |  |
| [[UQCR11]] | +0.84 | +0.78 / +0.84 | both halves | 7e-06 | STRING 717 |
| [[ATP5MJ]] | +0.83 | +0.75 / +0.85 | both halves | 7e-06 |  |
| [[ATP5ME]] | +0.83 | +0.68 / +0.86 | both halves | 7e-06 | STRING 427 |
| [[RPL36AL]] ⚠ | +0.83 | +0.75 / +0.84 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[COX6A1]] | +0.83 | +0.77 / +0.86 | both halves | 7e-06 | STRING 464 |
| [[COX6C]] | +0.82 | +0.75 / +0.83 | both halves | 7e-06 | STRING 631 |
| [[MIF]] | +0.82 | +0.76 / +0.85 | both halves | 7e-06 |  |
| [[UBL5]] | +0.82 | +0.77 / +0.82 | both halves | 7e-06 | STRING 482 |
| [[NDUFA1]] | +0.81 | +0.80 / +0.84 | both halves | 7e-06 | STRING 498 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF460]] | -0.68 | -0.50 / -0.68 | both halves | 1e-05 |  |
| [[NRAS]] | -0.67 | -0.45 / -0.68 | both halves | 3e-05 |  |
| [[U2AF2]] | -0.65 | -0.39 / -0.70 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.920). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.1, -22.0); signed map (-34.6, 9.2). **Vector** length 68.1, 31.9% of its response variance represented; |z| ≥ 3 in 471 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.74 to 31); *Respiratory electron transport* (reactome, mean cos +0.72 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.75 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | +3.0 | +3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +0.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +0.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.4 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +0.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +1.7 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM |  | +1.1 | +0.7 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | +1.1 | +0.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | -6.3 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | -6.2 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -5.9 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | +0.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -0.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.6 | +1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | reactive oxygen species modulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:35,699,272-35,700,984 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA353C18.2, MTGMP; previously C20orf52 |
| Gene groups (HGNC) | Tim17 family |
| Matched by | ensembl_id |

**Function**, from UniProt [P60602](https://www.uniprot.org/uniprotkb/P60602) (Reactive oxygen species modulator 1):

> Induces production of reactive oxygen species (ROS) which are necessary for cell proliferation. May play a role in inducing oxidative DNA damage and replicative senescence. May play a role in the coordination of mitochondrial morphology and cell proliferation.; Has antibacterial activity against a variety of bacteria including S.aureus, P.aeruginosa and M.tuberculosis. Acts by inducing bacterial membrane breakage.

**Summary**, from NCBI Gene [140823](https://www.ncbi.nlm.nih.gov/gene/140823):

> The protein encoded by this gene is a mitochondrial membrane protein that is responsible for increasing the level of reactive oxygen species (ROS) in cells. The protein also has antimicrobial activity against a variety of bacteria by inducing bacterial membrane breakage. [provided by RefSeq, Nov 2014]

**Accessions** — [HGNC:16185](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16185) · Entrez [140823](https://www.ncbi.nlm.nih.gov/gene/140823) · UniProt [P60602](https://www.uniprot.org/uniprotkb/P60602) · Ensembl [ENSG00000125995](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125995)

## Data

Gene col 4705: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4705); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4705, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4705]; `tensor/DDL_lfc|DDL_z.npy` [4705]; `embed/gene_vectors.npy` [4705]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4705 or target_col == 4705). Every well: [[ROMO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ROMO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
