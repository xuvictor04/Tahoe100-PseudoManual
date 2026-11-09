---
symbol: "DDX49"
type: "gene"
col: 2642
ensembl_id: "ENSG00000105671"
name: "DEAD-box helicase 49"
location: "19p13.11"
module: 210
arm: "+"
pooled_cpm: 11.28
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/210"]
generated_by: "tahoemap"
---

# DDX49

*DEAD-box helicase 49* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.53× (z +13.9, q 4e-41, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.606× (z -7.5, q 4e-11, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAGOH]] (+0.66, fdr 1e-05), [[NUP214]] (+0.66, fdr 7e-06), [[RTF2]] (+0.66, fdr 1e-05); moves opposite to [[PSPC1]] (-0.53, fdr 4e-05), [[MYEF2]] (-0.53, fdr 4e-05), [[SMC6]] (-0.52, fdr 1e-05).
> It is in [[Module 210]], a single-armed module (tRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2642.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.53×** | +13.9 | 4e-41 | 45/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +13.7 | 4e-40 | 36/44 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.36×** | +12.9 | 2e-35 | 42/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.00×** | +10.4 | 5e-23 | 41/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.94×** | +9.9 | 5e-21 | 34/46 (SW480, NCI-H460, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.14×** | +8.9 | 4e-17 | 30/43 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.79×** | +8.7 | 4e-16 | 23/38 (SNU-423, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.82×** | +8.3 | 8e-15 | 22/31 (PANC-1, LoVo, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.83×** | +8.1 | 3e-14 | 36/48 (SW480, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +8.1 | 3e-14 | 31/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +6.8 | 7e-10 | 25/45 (Panc 03.27, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +6.5 | 3e-09 | 26/46 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +6.4 | 7e-09 | 26/41 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.02×** | +5.5 | 2e-06 | 15/35 (A498, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +5.1 | 1e-05 | 21/47 (PANC-1, C32, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.59×** | +3.6 | 0.009 | 7/46 (SW480, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.021 | 7/48 (PANC-1, SHP-77, …) | all doses, flat | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.053 | 2/46 (SK-MEL-2, NCI-H1792) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.46×** | +2.9 | 0.070 | 2/41 (A-427, SW1417) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2642.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.606×** | -7.5 | 4e-11 | 28/46 (RPMI-7951, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.738×** | -6.4 | 3e-08 | 26/48 (A498, SW1417, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.784×** | -3.6 | 0.051 | 13/46 (A498, H4, …) | two highest doses | low cells (technical?) |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | 0.808× | -3.2 | 0.19 | 8/46 (NCI-H460, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2642. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 14.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.76× (z +10.9) | — |
| [[A498 (line)]] | wt | 14.5 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.433× (z -9.0) |
| [[A549 (line)]] | wt | 7.47 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.103× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 9.28 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.30× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 20.4 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.145× (z -10.0) |
| [[SHP-77 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0947× (z -10.3) |
| [[A-172 (line)]] | wt | 9.92 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2642), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGOH]] | +0.66 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[NUP214]] | +0.66 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[RTF2]] | +0.66 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[TRMT44]] | +0.64 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[SUPV3L1]] | +0.61 | +0.55 / +0.66 | both halves | 1e-05 | STRING 406 |
| [[TFIP11]] | +0.61 | +0.71 / +0.46 | both halves | 2e-05 |  |
| [[PMM2]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[TOMM70]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[SLC25A38]] | +0.60 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[RARS2]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[VPS51]] | +0.60 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[ACO2]] | +0.60 | +0.57 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSPC1]] | -0.53 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[MYEF2]] | -0.53 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[SMC6]] | -0.52 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[REEP3]] | -0.51 | -0.53 / -0.40 | both halves | 4e-05 |  |
| [[CREB1]] | -0.50 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[ANKRD50]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 210]] — tRNA processing; 13 genes; every member is in the + arm (projection on the module's main direction 0.828). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-24.7, -12.3); signed map (-32.4, -28.6). **Vector** length 67.2, 11.2% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +13.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +9.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.4 | +8.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +8.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +12.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +5.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | +3.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.3 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.9 | -7.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.5 | -1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 49 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,919,705-18,929,189 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10432, Dbp8 |
| Gene groups (HGNC) | DEAD-box helicases; SSU processome |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6V7](https://www.uniprot.org/uniprotkb/Q9Y6V7) (Probable ATP-dependent RNA helicase DDX49):

> ATP-dependent RNA helicase that plays a role in various aspects of RNA metabolism including the regulation of mRNA export and the levels of pre-ribosomal RNA. Regulates the stability and synthesis of pre-ribosomal RNA and thereby regulates cell proliferation. Also possesses antiviral activity by recognizing gammaherpesvirus transcripts in the context of lytic reactivation.

**Summary**, from NCBI Gene [54555](https://www.ncbi.nlm.nih.gov/gene/54555):

> Enables RNA helicase activity. Involved in positive regulation of cell growth and regulation of rRNA stability. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18684](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18684) · Entrez [54555](https://www.ncbi.nlm.nih.gov/gene/54555) · UniProt [Q9Y6V7](https://www.uniprot.org/uniprotkb/Q9Y6V7) · Ensembl [ENSG00000105671](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105671)

## Data

Gene col 2642: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2642); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2642, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2642]; `tensor/DDL_lfc|DDL_z.npy` [2642]; `embed/gene_vectors.npy` [2642]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2642 or target_col == 2642). Every well: [[DDX49 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX49.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
