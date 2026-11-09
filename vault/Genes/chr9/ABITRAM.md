---
symbol: "ABITRAM"
type: "gene"
col: 4054
ensembl_id: "ENSG00000119328"
name: "actin binding transcription modulator"
location: "9q31.3"
module: 17
arm: "+"
pooled_cpm: 15.71
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ABITRAM

*actin binding transcription modulator* — 9q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.60× (z +8.3, q 7e-14, up in 18 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.28× (z +6.3, q 3e-08, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.771× (z -6.7, q 1e-08, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAPPC11]] (+0.70, fdr 7e-06), [[DBT]] (+0.68, fdr 7e-06), [[RBM18]] (+0.67, fdr 7e-06); moves opposite to [[RBPMS2]] (-0.51, fdr 5e-05), [[DOCK9]] (-0.51, fdr 2e-05), [[MEGF11]] (-0.50, fdr 5e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4054.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +8.3 | 7e-14 | 18/27 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +7.9 | 8e-13 | 22/38 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.50×** | +7.1 | 3e-10 | 26/47 (SW480, A498, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +6.7 | 3e-09 | 15/30 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +6.3 | 3e-08 | 22/48 (A-172, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +6.1 | 8e-08 | 24/47 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.21×** | +4.9 | 8e-05 | 18/47 (PANC-1, NCI-H23, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 3e-04 | 17/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.27×** | +4.3 | 9e-04 | 12/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +4.1 | 0.003 | 11/48 (HEC-1-A, NCI-H2347, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.24×** | +3.9 | 0.004 | 17/45 (KATO III, HEC-1-A, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.006 | 12/47 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Terfenadine (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.006 | 5/47 (NCI-H460, MIA PaCa-2, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.027 | 10/47 (Hs 766T, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.052 | 4/46 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Aliskiren (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.073 | 9/47 (Hs 766T, LoVo, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4054.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.771×** | -6.7 | 1e-08 | 26/48 (NCI-H460, LoVo, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.717×** | -6.1 | 4e-07 | 20/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.819×** | -5.1 | 5e-05 | 22/45 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **0.790×** | -4.3 | 0.002 | 13/45 (PANC-1, NCI-H2030, …) | two highest doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.879× | -3.3 | 0.11 | 15/48 (CHP-212, SW 1271, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.882× | -3.2 | 0.12 | 13/48 (MIA PaCa-2, HOP62, …) | top dose only | position effect removed |
| [[Folic acid (drug)]] 5 µM |  | 0.886× | -3.1 | 0.14 | 4/48 (SW 1088, HEC-1-A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4054. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 11.5 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0592× (z -11.3) |
| [[A-427 (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4054), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC11]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[DBT]] | +0.68 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[RBM18]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[MKS1]] | +0.67 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[DYNC2LI1]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[BLTP1]] | +0.65 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[TMEM254]] | +0.64 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[SLC25A46]] | +0.63 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[UFSP2]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[CCDC113]] | +0.62 | +0.39 / +0.69 | both halves | 5e-05 |  |
| [[PTCD2]] | +0.62 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[ASB8]] | +0.62 | +0.68 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBPMS2]] | -0.51 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[DOCK9]] | -0.51 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[MEGF11]] | -0.50 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[MAD1L1]] | -0.49 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[CTBP2]] | -0.49 | -0.39 / -0.43 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.613). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.3, 1.6); signed map (-20.8, -16.8). **Vector** length 66.1, 10.1% of its response variance represented; |z| ≥ 3 in 831 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Intraflagellar transport* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.8 | +6.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.7 | +6.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.1 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +4.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +2.2 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.6 | +1.9 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +1.3 | +3.8 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | +1.2 | +0.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.8 | -6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -5.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | +0.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | actin binding transcription modulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.3 — chr9:108,934,400-108,950,744 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CG-8, FLJ20457, Simiate; previously C9orf6, FAM206A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX38](https://www.uniprot.org/uniprotkb/Q9NX38) (Protein Abitram):

> Actin-binding protein that regulates actin polymerization, filopodia dynamics and increases the branching of proximal dendrites of developing neurons.

**Summary**, from NCBI Gene [54942](https://www.ncbi.nlm.nih.gov/gene/54942):

> Predicted to enable actin filament binding activity and actin monomer binding activity. Predicted to be involved in dendrite morphogenesis; regulation of actin filament polymerization; and regulation of filopodium assembly. Predicted to be located in growth cone. Predicted to be active in several cellular components, including dendrite; filopodium tip; and lamellipodium. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1364](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1364) · Entrez [54942](https://www.ncbi.nlm.nih.gov/gene/54942) · UniProt [Q9NX38](https://www.uniprot.org/uniprotkb/Q9NX38) · Ensembl [ENSG00000119328](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119328)

## Data

Gene col 4054: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4054); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4054, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4054]; `tensor/DDL_lfc|DDL_z.npy` [4054]; `embed/gene_vectors.npy` [4054]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4054 or target_col == 4054). Every well: [[ABITRAM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABITRAM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
