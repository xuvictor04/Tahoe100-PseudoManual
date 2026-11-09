---
symbol: "ATP5MC2"
type: "gene"
col: 5696
ensembl_id: "ENSG00000135390"
name: "ATP synthase membrane subunit c locus 2"
location: "12q13.13"
module: 43
arm: "+"
pooled_cpm: 66.43
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# ATP5MC2

*ATP synthase membrane subunit c locus 2* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.23× (z +6.1, q 7e-07, up in 42 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.628× (z -5.1, q 2e-04, down in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.142×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 28 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TOMM7]] (+0.89, fdr 7e-06), [[NACA4P]] (+0.85, fdr 7e-06, ⚠ NACA4P in the vector space only through flagged drug-doses), [[RPL36]] (+0.83, fdr 7e-06), [[RPL35A]] (+0.80, fdr 7e-06); moves opposite to [[PSME3]] (-0.75, fdr 7e-06), [[DBNL]] (-0.68, fdr 1e-05), [[MAPRE1]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5696.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.23×** | +6.1 | 7e-07 | 42/49 (HT-29, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +4.7 | 8e-04 | 37/43 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.59×** | +3.7 | 0.047 | 31/48 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.51× | +3.2 | 0.22 | 29/47 (HepG2/C3A, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5696.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.142×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.628×** | -5.1 | 2e-04 | 40/48 (A-427, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | 0.643× | -3.4 | 0.16 | 36/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.658× | -3.0 | 0.33 | 35/48 (LoVo, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5696. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 35.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -10.8) |
| [[A-172 (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 61.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 76.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 77.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 67.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 76.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 78.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 92.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 79.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 91.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5696), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 28 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 6 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOMM7]] | +0.89 | +0.82 / +0.91 | both halves | 7e-06 |  |
| [[NACA4P]] ⚠ | +0.85 | +0.76 / +0.86 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36]] | +0.83 | +0.73 / +0.86 | both halves | 7e-06 | STRING 432 |
| [[RPS27A]] ⚠ | +0.82 | +0.72 / +0.86 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; ⚠ in the vector space only through flagged drug-doses |
| [[RPL18]] ⚠ | +0.81 | +0.71 / +0.85 | both halves | 7e-06 | STRING 537; ⚠ in the vector space only through flagged drug-doses |
| [[UQCRB]] ⚠ | +0.81 | +0.78 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 511; ⚠ in the vector space only through flagged drug-doses |
| [[RPL35A]] | +0.80 | +0.70 / +0.84 | both halves | 7e-06 | STRING 432 |
| [[SMIM26]] ⚠ | +0.80 | +0.71 / +0.83 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG6]] | +0.80 | +0.69 / +0.81 | both halves | 7e-06 |  |
| [[RPL31]] | +0.80 | +0.68 / +0.84 | both halves | 7e-06 |  |
| [[RPS3]] ⚠ | +0.80 | +0.69 / +0.81 | both halves | 7e-06 | STRING 772; ⚠ in the vector space only through flagged drug-doses |
| [[RPL34]] | +0.79 | +0.69 / +0.84 | both halves | 7e-06 |  |
| [[RPS27]] | +0.78 | +0.70 / +0.82 | both halves | 7e-06 |  |
| [[RPL23]] | +0.77 | +0.65 / +0.82 | both halves | 7e-06 | STRING 698 |
| [[ATP5ME]] | +0.76 | +0.63 / +0.77 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 991 |
| [[RPS19]] | +0.76 | +0.69 / +0.79 | both halves | 7e-06 |  |
| [[SNHG19]] | +0.76 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[RPS8]] | +0.76 | +0.65 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.75 | -0.63 / -0.76 | both halves | 7e-06 |  |
| [[DBNL]] | -0.68 | -0.53 / -0.70 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.66 | -0.52 / -0.71 | both halves | 1e-05 | pathway: Organelle biogenesis and maintenance |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.777). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-43.7, -26.4); signed map (-58.6, -3.2). **Vector** length 73.8, 29.9% of its response variance represented; |z| ≥ 3 in 432 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.64 to 55); *Peptide chain elongation* (reactome, mean cos +0.65 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.64 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +1.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | -0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | -0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +2.2 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.5 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.4 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -0.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.6 | +0.7 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -0.7 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | ATP synthase membrane subunit c locus 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,632,726-53,677,408 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ATP5G2 |
| Gene groups (HGNC) | Mitochondrial complex V: ATP synthase subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 5 pathways, smallest: Formation of ATP by chemiosmotic coupling; Cristae formation; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06055](https://www.uniprot.org/uniprotkb/Q06055) (ATP synthase F(0) complex subunit C2, mitochondrial):

> Mitochondrial membrane ATP synthase (F(1)F(0) ATP synthase or Complex V) produces ATP from ADP in the presence of a proton gradient across the membrane which is generated by electron transport complexes of the respiratory chain. F-type ATPases consist of two structural domains, F(1) - containing the extramembraneous catalytic core and F(0) - containing the membrane proton channel, linked together by a central stalk and a peripheral stalk. During catalysis, ATP synthesis in the catalytic domain …

**Summary**, from NCBI Gene [517](https://www.ncbi.nlm.nih.gov/gene/517):

> This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic portion of mitochondrial ATP synthase consists of 5 different subunits (alpha, beta, gamma, …

**Accessions** — [HGNC:842](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:842) · Entrez [517](https://www.ncbi.nlm.nih.gov/gene/517) · UniProt [Q06055](https://www.uniprot.org/uniprotkb/Q06055) · Ensembl [ENSG00000135390](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135390)

## Data

Gene col 5696: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5696); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5696, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5696]; `tensor/DDL_lfc|DDL_z.npy` [5696]; `embed/gene_vectors.npy` [5696]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5696 or target_col == 5696). Every well: [[ATP5MC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP5MC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
