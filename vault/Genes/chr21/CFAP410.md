---
symbol: "CFAP410"
type: "gene"
col: 8326
ensembl_id: "ENSG00000160226"
name: "cilia and flagella associated protein 410"
location: "21q22.3"
module: 157
arm: "+"
pooled_cpm: 2.66
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# CFAP410

*cilia and flagella associated protein 410* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.64× (z +10.0, q 6e-21, up in 2 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM: 1.48× (z +4.2, q 0.004, up in 4 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.655× (z -4.5, q 0.001, down in 15 of 44 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.658× (z -4.5, q 0.001, down in 7 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC9A3-AS1]] (+0.61, fdr 8e-06), [[WDR6]] (+0.60, fdr 1e-05), [[PAQR6]] (+0.59, fdr 3e-05).
> It is in [[Module 157]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8326.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.64×** | +10.0 | 6e-21 | 2/4 (A498, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.33×** | +9.1 | 3e-17 | 6/13 (Hs 766T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +7.9 | 7e-13 | 3/5 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.48×** | +4.2 | 0.004 | 4/28 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.63×** | +3.8 | 0.020 | 2/32 (PANC-1, BT-474) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.43×** | +3.5 | 0.036 | 3/26 (SHP-77, RKO, …) | inconsistent across doses | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.87×** | +3.5 | 0.036 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +3.4 | 0.044 | 6/12 (A-427, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.094 | 2/44 (HEC-1-A, SW48) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.33× | +3.1 | 0.11 | 3/31 (NCI-H1573, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8326.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.655×** | -4.5 | 0.001 | 15/44 (HepG2/C3A, C-33 A, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.656×** | -4.5 | 0.001 | 11/44 (H4, NCI-H1573, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.658×** | -4.5 | 0.001 | 7/31 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.764×** | -4.1 | 0.006 | 13/34 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.705×** | -3.8 | 0.019 | 6/44 (SW1417, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.708×** | -3.7 | 0.019 | 12/42 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Eplerenone (drug)]] 5 µM |  | **0.724×** | -3.3 | 0.061 | 6/43 (LS 180, RKO, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.733×** | -3.3 | 0.061 | 7/43 (H4, A549, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.741×** | -3.2 | 0.079 | 6/43 (J82, HT-29, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.744×** | -3.2 | 0.086 | 9/44 (COLO 205, LS 180, …) | two highest doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.748×** | -3.1 | 0.094 | 6/42 (HOP62, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8326. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 1271 (line)]] | alt | 2.10 | 0 | 1 | — | [[Pentagastrin (drug)]] 5 µM 0.155× (z -9.6) |
| [[SW1417 (line)]] | alt | 3.39 | 0 | 1 | — | [[Neratinib (drug)]] 0.05 µM 0.0782× (z -8.5) |
| [[SW480 (line)]] | alt | 2.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -8.5) |
| [[A-172 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8326), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A3-AS1]] | +0.61 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[WDR6]] | +0.60 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[PAQR6]] | +0.59 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[GET4]] | +0.58 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[ZBTB22]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[FAM229A]] | +0.57 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[MAMDC4]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[LMNTD2]] | +0.57 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[PLA2G4B]] | +0.56 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[MIB2]] | +0.55 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[LZTS3]] | +0.55 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[IL11RA]] | +0.55 | +0.49 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-14.3, -24.5); signed map (-0.4, 4.7). **Vector** length 32.1, 2.56% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +7.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.8 | +3.4 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +1.6 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +3.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +2.8 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.1 | +2.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.5 | -3.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -2.8 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.0 | +0.1 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -0.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.0 | -2.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.9 | -1.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 410 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:44,328,944-44,339,402 (-) |
| Ensembl biotype | protein_coding |
| Also known as | YF5, A2, LRRC76; previously C21orf2 |
| Matched by | ensembl_id |

**Function**, from UniProt [O43822](https://www.uniprot.org/uniprotkb/O43822) (Cilia- and flagella-associated protein 410):

> Plays a role in cilia formation and/or maintenance (By similarity). Plays a role in the regulation of cell morphology and cytoskeletal organization. Involved in DNA damage repair.

**Summary**, from NCBI Gene [755](https://www.ncbi.nlm.nih.gov/gene/755):

> Four alternatively spliced transcript variants encoding four different isoforms have been found for this nuclear gene. All isoforms contain leucine-rich repeats. Three of these isoforms are mitochondrial proteins and one of them lacks the target peptide, so is not located in mitochondrion. This gene is down-regulated in Down syndrome (DS) brain, which may represent mitochondrial dysfunction in DS patients. [provided by RefSeq, Sep 2012]

**Accessions** — [HGNC:1260](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1260) · Entrez [755](https://www.ncbi.nlm.nih.gov/gene/755) · UniProt [O43822](https://www.uniprot.org/uniprotkb/O43822) · Ensembl [ENSG00000160226](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160226)

## Data

Gene col 8326: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8326); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8326, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8326]; `tensor/DDL_lfc|DDL_z.npy` [8326]; `embed/gene_vectors.npy` [8326]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8326 or target_col == 8326). Every well: [[CFAP410 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP410.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
