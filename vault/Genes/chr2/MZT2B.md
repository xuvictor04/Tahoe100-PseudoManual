---
symbol: "MZT2B"
type: "gene"
col: 7589
ensembl_id: "ENSG00000152082"
name: "mitotic spindle organizing protein 2B"
location: "2q21.1"
module: 131
arm: "+"
pooled_cpm: 34.82
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# MZT2B

*mitotic spindle organizing protein 2B* — 2q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.15× (z +7.5, q 4e-11, up in 42 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.451× (z -7.2, q 2e-10, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MZT2A]] (+0.89, fdr 7e-06), [[NENF]] (+0.81, fdr 7e-06), [[RPLP2]] (+0.80, fdr 7e-06); moves opposite to [[PDAP1]] (-0.69, fdr 7e-06), [[EIF4G1]] (-0.67, fdr 7e-06), [[ZNF460]] (-0.67, fdr 1e-05).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7589.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.15×** | +7.5 | 4e-11 | 42/44 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.98×** | +6.8 | 3e-09 | 36/37 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +5.4 | 1e-05 | 36/41 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **2.12×** | +4.9 | 2e-04 | 39/46 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.83×** | +3.9 | 0.010 | 39/47 (NCI-H460, SW480, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 2.17× | +3.0 | 0.25 | 33/47 (SHP-77, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7589.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.451×** | -7.2 | 2e-10 | 45/47 (H4, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.455×** | -5.1 | 1e-04 | 41/47 (RPMI-7951, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.558×** | -3.8 | 0.033 | 31/48 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.67 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7589. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 24.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -12.1) |
| [[H4 (line)]] | wt | 37.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0704× (z -16.7) |
| [[HOP62 (line)]] | alt | 35.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -11.1) |
| [[J82 (line)]] | alt | 31.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 39.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -12.7) |
| [[NCI-H2030 (line)]] | alt | 60.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 32.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -9.1) |
| [[SNU-1 (line)]] | wt | 39.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 33.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0804× (z -10.0) |
| [[A-172 (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 34.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7589), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 16 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MZT2A]] | +0.89 | +0.90 / +0.89 | both halves | 7e-06 | pathway: Centrosome maturation; STRING 870 |
| [[NENF]] | +0.81 | +0.84 / +0.75 | both halves | 7e-06 |  |
| [[RPLP2]] | +0.80 | +0.78 / +0.77 | both halves | 7e-06 |  |
| [[RPS29]] | +0.78 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[NDUFB11]] ⚠ | +0.77 | +0.66 / +0.75 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[UQCRB]] ⚠ | +0.77 | +0.65 / +0.75 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[COX4I1]] ⚠ | +0.76 | +0.60 / +0.76 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS21]] | +0.76 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[TOMM7]] | +0.76 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[MIF]] | +0.76 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[RPLP1]] | +0.75 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[COX7C]] | +0.74 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[SNHG25]] | +0.74 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[RPS19]] | +0.74 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[RPL35A]] | +0.74 | +0.65 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDAP1]] | -0.69 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[EIF4G1]] | -0.67 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[ZNF460]] | -0.67 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[CCT7]] | -0.67 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[SLC35A4]] | -0.65 | -0.74 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.746). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-46.1, -24.7); signed map (-35.8, 8.1). **Vector** length 64.1, 20.9% of its response variance represented; |z| ≥ 3 in 538 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Termination* (reactome, mean cos +0.65 to 20); *Peptide chain elongation* (reactome, mean cos +0.66 to 19); *PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA* (reactome, mean cos +0.66 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +3.8 | +3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.4 | -0.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | +0.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.4 | -7.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | mitotic spindle organizing protein 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.1 — chr2:130,181,737-130,190,729 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14346, MOZART2B; previously FAM128B |
| Reactome | 9 pathways, smallest: Centrosome maturation; Recruitment of mitotic centrosome proteins and complexes; Recruitment of NuMA to mitotic centrosomes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NZ67](https://www.uniprot.org/uniprotkb/Q6NZ67) (Mitotic-spindle organizing protein 2B):

> Required for the recruitment and the assembly of the gamma-tubulin ring complex (gTuRC) at the centrosome. The gTuRC regulates the minus-end nucleation of alpha-beta tubulin heterodimers that grow into microtubule protafilaments, a critical step in centrosome duplication and spindle formation.

**Summary**, from NCBI Gene [80097](https://www.ncbi.nlm.nih.gov/gene/80097):

> Predicted to be involved in microtubule nucleation. Located in centrosome and spindle. Part of gamma-tubulin ring complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25886](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25886) · Entrez [80097](https://www.ncbi.nlm.nih.gov/gene/80097) · UniProt [Q6NZ67](https://www.uniprot.org/uniprotkb/Q6NZ67) · Ensembl [ENSG00000152082](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152082)

## Data

Gene col 7589: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7589); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7589, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7589]; `tensor/DDL_lfc|DDL_z.npy` [7589]; `embed/gene_vectors.npy` [7589]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7589 or target_col == 7589). Every well: [[MZT2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MZT2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
