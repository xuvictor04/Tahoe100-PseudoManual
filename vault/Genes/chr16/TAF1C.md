---
symbol: "TAF1C"
type: "gene"
col: 2329
ensembl_id: "ENSG00000103168"
name: "TATA-box binding protein associated factor, RNA polymerase I subunit C"
location: "16q24.1"
module: 96
arm: "+"
pooled_cpm: 7.22
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# TAF1C

*TATA-box binding protein associated factor, RNA polymerase I subunit C* — 16q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.71× (z +9.0, q 1e-16, up in 28 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.123×); [[Pimozide (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0924×); [[Rutin (trihydrate) (drug)]] 5 µM in 1 line (SW48 0.0565×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHOT2]] (+0.76, fdr 7e-06), [[ARFRP1]] (+0.73, fdr 7e-06), [[WIZ]] (+0.71, fdr 7e-06); moves opposite to [[COX8A]] (-0.51, fdr 3e-05), [[SLC25A5]] (-0.48, fdr 5e-05).
> It is in [[Module 096]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2329.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +9.0 | 1e-16 | 28/43 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +7.0 | 6e-10 | 27/47 (NCI-H1573, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.79×** | +6.9 | 7e-10 | 31/47 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +6.7 | 4e-09 | 23/42 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +6.1 | 1e-07 | 6/14 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +5.9 | 3e-07 | 25/46 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.65×** | +5.3 | 8e-06 | 19/46 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +5.2 | 1e-05 | 21/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +4.9 | 7e-05 | 9/22 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.003 | 13/47 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.39×** | +3.7 | 0.010 | 10/46 (SW480, BT-474, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.6 | 0.013 | 3/24 (MIA PaCa-2, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.013 | 11/45 (AN3 CA, SW 900, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.53×** | +3.6 | 0.013 | 11/44 (KATO III, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.026 | 10/45 (NCI-H23, SW480, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.036 | 7/44 (LOX-IMVI, Panc 03.27, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.038 | 4/47 (HS-578T, Hs 766T, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.44×** | +3.1 | 0.056 | 8/41 (J82, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.42×** | +2.9 | 0.088 | 5/38 (HS-578T, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2329.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.123×); [[Pimozide (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0924×); [[Rutin (trihydrate) (drug)]] 5 µM in 1 line (SW48 0.0565×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.753× | -3.4 | 0.37 | 7/47 (HepG2/C3A, NCI-H2030, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.778× | -3.0 | 0.64 | 5/47 (SW 1088, NCI-H661, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2329. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 8.00 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0924× (z -9.0) |
| [[SHP-77 (line)]] | alt | 10.9 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.123× (z -9.1) |
| [[SW48 (line)]] | wt | 9.68 | 0 | 1 | — | [[Rutin (trihydrate) (drug)]] 5 µM 0.0565× (z -8.5) |
| [[A-172 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2329), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOT2]] | +0.76 | +0.77 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[ARFRP1]] | +0.73 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[WIZ]] | +0.71 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[NCDN]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[WDR6]] | +0.67 | +0.60 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[PLEKHG4]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[ZNF513]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[EDC4]] | +0.65 | +0.71 / +0.67 | both halves | 7e-06 | STRING 538 |
| [[TEPSIN]] | +0.65 | +0.71 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[DMAP1]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[CACTIN]] | +0.63 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[HGS]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX8A]] | -0.51 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[SLC25A5]] | -0.48 | -0.39 / -0.50 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.728). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-12.3, -24.7); signed map (-9.2, -32.0). **Vector** length 59.9, 8.85% of its response variance represented; |z| ≥ 3 in 722 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.9 | +7.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +3.1 | +3.3 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.9 | +3.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.6 | +2.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.6 | +3.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.3 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +3.3 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -3.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.8 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -0.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor, RNA polymerase I subunit C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.1 — chr16:84,177,847-84,187,070 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TAFI110, TAFI95, SL1, MGC:39976 |
| Hallmark sets | DNA_REPAIR |
| Reactome | 10 pathways, smallest: SIRT1 negatively regulates rRNA expression; RNA Polymerase I Transcription Termination; B-WICH complex positively regulates rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15572](https://www.uniprot.org/uniprotkb/Q15572) (TATA box-binding protein-associated factor RNA polymerase I subunit C):

> Component of the transcription factor SL1/TIF-IB complex, which is involved in the assembly of the PIC (pre-initiation complex) during RNA polymerase I-dependent transcription. The rate of PIC formation probably is primarily dependent on the rate of association of SL1/TIF-IB with the rDNA promoter. SL1/TIF-IB is involved in stabilization of nucleolar transcription factor 1/UBTF on rDNA. Formation of SL1/TIF-IB excludes the association of TBP with TFIID subunits. Recruits RNA polymerase I to the …

**Summary**, from NCBI Gene [9013](https://www.ncbi.nlm.nih.gov/gene/9013):

> Initiation of transcription by RNA polymerase I requires the formation of a complex composed of the TATA-binding protein (TBP) and three TBP-associated factors (TAFs) specific for RNA polymerase I. This complex, known as SL1, binds to the core promoter of ribosomal RNA genes to position the polymerase properly and acts as a channel for regulatory signals. This gene encodes the largest SL1-specific TAF. Multiple alternatively spliced transcript variants encoding different isoforms have been …

**Accessions** — [HGNC:11534](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11534) · Entrez [9013](https://www.ncbi.nlm.nih.gov/gene/9013) · UniProt [Q15572](https://www.uniprot.org/uniprotkb/Q15572) · Ensembl [ENSG00000103168](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103168)

## Data

Gene col 2329: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2329); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2329, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2329]; `tensor/DDL_lfc|DDL_z.npy` [2329]; `embed/gene_vectors.npy` [2329]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2329 or target_col == 2329). Every well: [[TAF1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
