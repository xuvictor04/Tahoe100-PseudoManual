---
symbol: "ZNF74"
type: "gene"
col: 11647
ensembl_id: "ENSG00000185252"
name: "zinc finger protein 74"
location: "22q11.21"
module: 33
arm: "+"
pooled_cpm: 5.12
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# ZNF74

*zinc finger protein 74* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.19× (z +10.1, q 4e-21, up in 23 of 30 measured lines) ⚠ toxic. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.35× (z +5.6, q 6e-06, up in 12 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.302× (z -15.9, q 0e+00, down in 40 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS26]] (+0.80, fdr 7e-06), [[PET117]] (+0.73, fdr 1e-05), [[KAT14]] (+0.71, fdr 1e-05); moves opposite to [[TTC41P]] (-0.58, fdr 3e-05), [[CCNT2-AS1]] (-0.58, fdr 6e-05), [[ENSA]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11647.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +10.1 | 4e-21 | 23/30 (C-33 A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +5.6 | 6e-06 | 12/46 (C32, MIA PaCa-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +5.3 | 3e-05 | 10/45 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +4.6 | 7e-04 | 12/43 (NCI-H2347, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.025 | 6/45 (SW480, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.027 | 12/46 (NCI-H1573, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +3.6 | 0.027 | 6/46 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.046 | 5/34 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.046 | 6/44 (LoVo, LOX-IMVI, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | 1.26× | +3.0 | 0.14 | 7/43 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11647.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.302×** | -15.9 | 0e+00 | 40/46 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.413×** | -11.8 | 1e-29 | 37/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.503×** | -9.2 | 9e-18 | 22/37 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.561×** | -7.7 | 2e-12 | 24/45 (HT-29, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.705×** | -6.6 | 5e-09 | 23/39 (J82, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.711×** | -6.4 | 1e-08 | 20/38 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~19% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.739×** | -4.0 | 0.004 | 20/44 (NCI-H23, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.593×** | -3.6 | 0.019 | 9/43 (LOX-IMVI, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.773×** | -3.4 | 0.037 | 12/46 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11647. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.02 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.163× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 5.78 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -15.9) |
| [[SW1417 (line)]] | alt | 9.99 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -10.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 5.03 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0834× (z -8.7) |
| [[Hs 766T (line)]] | wt | 4.64 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0908× (z -8.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 3.95 | 0 | 1 | — | [[Peretinoin (drug)]] 0.5 µM 0.0669× (z -8.8) |
| [[HT-29 (line)]] | alt | 3.89 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0667× (z -9.8) |
| [[J82 (line)]] | alt | 2.53 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0943× (z -10.8) |
| [[LS 180 (line)]] | wt | 5.39 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.120× (z -9.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 9.55 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0686× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[NCI-H1573 (line)]] | alt | 3.66 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0524× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 6.66 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.111× (z -9.3) |
| [[RKO (line)]] | wt | 8.15 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.119× (z -9.0) ⚠ transcription drop |
| [[SW48 (line)]] | wt | 13.3 | 0 | 1 | — | [[Ponatinib (drug)]] 0.5 µM 0.0740× (z -10.0) |
| [[A-172 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11647), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS26]] | +0.80 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[PET117]] | +0.73 | +0.56 / +0.74 | both halves | 1e-05 |  |
| [[KAT14]] | +0.71 | +0.57 / +0.75 | both halves | 1e-05 |  |
| [[ORC5]] | +0.70 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[TMEM177]] | +0.68 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[NLE1]] | +0.68 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[CDPF1]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[MRPS23]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[DDX55]] | +0.67 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[GEMIN5]] | +0.66 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[ZNF30]] | +0.66 | +0.55 / +0.64 | both halves | 1e-05 | same gene group |
| [[GTF2H2]] | +0.66 | +0.55 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC41P]] | -0.58 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[CCNT2-AS1]] | -0.58 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[ENSA]] | -0.55 | -0.48 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.692). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-45.2, -8.0); signed map (-16.4, -23.2). **Vector** length 61.0, 8.70% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +10.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.0 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.6 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | +0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.3 | +1.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.3 | -15.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -6.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.8 | -9.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.4 | -7.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -0.9 | +0.2 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 74 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:20,394,115-20,408,461 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Cos52, Zfp520, ZNF520 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16587](https://www.uniprot.org/uniprotkb/Q16587) (Zinc finger protein 74):

> May play a role in RNA metabolism.

**Summary**, from NCBI Gene [7625](https://www.ncbi.nlm.nih.gov/gene/7625):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13144](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13144) · Entrez [7625](https://www.ncbi.nlm.nih.gov/gene/7625) · UniProt [Q16587](https://www.uniprot.org/uniprotkb/Q16587) · Ensembl [ENSG00000185252](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185252)

## Data

Gene col 11647: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11647); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11647, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11647]; `tensor/DDL_lfc|DDL_z.npy` [11647]; `embed/gene_vectors.npy` [11647]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11647 or target_col == 11647). Every well: [[ZNF74 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF74.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
