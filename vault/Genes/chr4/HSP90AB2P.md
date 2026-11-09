---
symbol: "HSP90AB2P"
type: "gene"
col: 13026
ensembl_id: "ENSG00000205940"
name: "heat shock protein 90 alpha family class B member 2, pseudogene"
location: "4p15.33"
module: 60
arm: "+"
pooled_cpm: 4.39
n_lines_expressing: 46
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# HSP90AB2P

*heat shock protein 90 alpha family class B member 2, pseudogene* — 4p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 4.28× (z +10.9, q 1e-24, up in 40 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SW480 0.133×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSP90AB3P]] (+0.95, fdr 7e-06), [[HSP90AB1]] (+0.85, fdr 7e-06), [[HSP90AA2P]] (+0.79, fdr 7e-06); moves opposite to [[SKA2]] (-0.54, fdr 2e-05), [[ZC3H7B]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13026.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **4.28×** | +10.9 | 1e-24 | 40/43 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.85×** | +10.1 | 2e-21 | 41/42 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **3.50×** | +9.4 | 1e-18 | 39/42 (SW480, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.16×** | +8.6 | 1e-15 | 19/22 (J82, MIA PaCa-2, …) | all doses, flat | composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.38×** | +8.6 | 1e-15 | 36/40 (NCI-H2347, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.06×** | +8.0 | 8e-14 | 6/8 (NCI-H2347, MIA PaCa-2, …) | all doses, flat | composition shift; position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **6.64×** | +7.4 | 1e-11 | 17/17 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.87×** | +7.3 | 2e-11 | 9/11 (J82, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **2.17×** | +5.8 | 5e-07 | 28/42 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **3.82×** | +5.2 | 9e-06 | 23/30 (MIA PaCa-2, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.33×** | +4.5 | 3e-04 | 19/42 (CFPAC-1, NCI-H2347, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +4.2 | 0.002 | 14/44 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.67×** | +3.7 | 0.011 | 13/28 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.54×** | +3.2 | 0.048 | 6/43 (SNU-423, A-172, …) | rises with dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SW480 0.133×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13026. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 3.91 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.133× (z -9.0) |
| [[A-172 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.853 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.867 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.851 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13026), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSP90AB3P]] | +0.95 | +0.94 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[HSP90AB1]] | +0.85 | +0.86 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[HSP90AA2P]] | +0.79 | +0.78 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[HSPD1]] | +0.76 | +0.77 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[CCT4]] | +0.73 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[HSP90AA1]] | +0.70 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[CACYBP]] | +0.68 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[PWWP3A]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[HSPA8]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[SOD1]] | +0.66 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[ATP2C1]] | +0.65 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[CCT3]] | +0.64 | +0.67 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKA2]] | -0.54 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[ZC3H7B]] | -0.52 | -0.45 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.822). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.1, -11.4); signed map (-26.1, -28.6). **Vector** length 55.5, 8.17% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *heat shock* (control, mean cos +0.57 to 13); *Attenuation phase* (reactome, mean cos +0.59 to 13); *HSF1-dependent transactivation* (reactome, mean cos +0.59 to 14).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.0 | +9.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.7 | +8.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.4 | +10.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.9 | +10.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.4 | +7.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +2.2 |
|  | [[Infigratinib (drug)]] 5 µM |  | +1.1 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -0.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | +0.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.1 | -1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.1 | -1.0 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | -1.0 | -1.5 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.0 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein 90 alpha family class B member 2, pseudogene |
| Locus type | pseudogene |
| Location | 4p15.33 — chr4:13,336,482-13,338,657 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Also known as | HSP90BB |
| Matched by | ensembl_id |

**Function**, from UniProt [Q58FF8](https://www.uniprot.org/uniprotkb/Q58FF8) (Putative heat shock protein HSP 90-beta 2):

> Putative molecular chaperone that may promote the maturation, structural maintenance and proper regulation of specific target proteins.

**Summary**, from NCBI Gene [391634](https://www.ncbi.nlm.nih.gov/gene/391634):

> Predicted to enable ATP binding activity; ATP hydrolysis activity; and unfolded protein binding activity. Predicted to be involved in cellular response to heat; protein folding; and protein stabilization. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:32537](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32537) · Entrez [391634](https://www.ncbi.nlm.nih.gov/gene/391634) · UniProt [Q58FF8](https://www.uniprot.org/uniprotkb/Q58FF8) · Ensembl [ENSG00000205940](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205940)

## Data

Gene col 13026: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13026); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13026, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13026]; `tensor/DDL_lfc|DDL_z.npy` [13026]; `embed/gene_vectors.npy` [13026]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13026 or target_col == 13026). Every well: [[HSP90AB2P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSP90AB2P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
