---
symbol: "ATP5MC1"
type: "gene"
col: 8226
ensembl_id: "ENSG00000159199"
name: "ATP synthase membrane subunit c locus 1"
location: "17q21.32"
module: 58
arm: "+"
pooled_cpm: 21.94
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# ATP5MC1

*ATP synthase membrane subunit c locus 1* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.02× (z +7.9, q 1e-12, up in 27 of 30 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Arbutin (drug)]] 5 µM: 1.85× (z +3.5, q 0.046, up in 36 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (A-172 0.116×; ⚠ cell-cycle shift, explains ~49% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.239×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL12]] (+0.67, fdr 9e-06), [[CYC1]] (+0.62, fdr 4e-05), [[DNPH1]] (+0.62, fdr 1e-05); moves opposite to [[BROX]] (-0.57, fdr 4e-05), [[SNHG22]] (-0.55, fdr 2e-04), [[RMND5A]] (-0.55, fdr 2e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8226.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **4.02×** | +7.9 | 1e-12 | 27/30 (NCI-H460, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **4.92×** | +7.7 | 5e-12 | 39/41 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.77×** | +5.6 | 4e-06 | 31/35 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | **1.91×** | +3.9 | 0.016 | 28/45 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Arbutin (drug)]] 5 µM |  | **1.85×** | +3.5 | 0.046 | 36/46 (SNU-1, A-427, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.78×** | +3.3 | 0.083 | 25/44 (CFPAC-1, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change | **1.74×** | +3.3 | 0.083 | 29/46 (NCI-H460, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 1.69× | +3.0 | 0.19 | 25/47 (LOX-IMVI, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8226.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (A-172 0.116×; ⚠ cell-cycle shift, explains ~49% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.239×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.270× | -3.6 | 0.18 | 33/46 (SNU-1, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.77 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8226. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 14.7 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.116× (z -9.6) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SHP-77 (line)]] | alt | 28.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -9.0) |
| [[A-427 (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8226), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 13 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL12]] | +0.67 | +0.57 / +0.65 | both halves | 9e-06 | STRING 596 |
| [[CYC1]] | +0.62 | +0.41 / +0.74 | both halves | 4e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 947 |
| [[DNPH1]] | +0.62 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[NDUFA3]] | +0.62 | +0.44 / +0.62 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 677 |
| [[NHP2]] | +0.61 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[ATP5MF]] | +0.60 | +0.53 / +0.65 | both halves | 1e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 997 |
| [[AURKAIP1]] | +0.60 | +0.37 / +0.63 | both halves | 7e-05 | STRING 594 |
| [[UQCR10]] ⚠ | +0.59 | +0.36 / +0.64 | both halves | 1e-04 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 794; ⚠ in the vector space only through flagged drug-doses |
| [[TMEM147]] | +0.59 | +0.39 / +0.59 | both halves | 5e-05 | pathway: Protein localization |
| [[NDUFA7]] | +0.59 | +0.31 / +0.67 | both halves | 2e-04 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 553 |
| [[TMEM160]] | +0.57 | +0.29 / +0.57 | both halves | 2e-04 |  |
| [[COX8A]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 641 |
| [[TXNDC17]] | +0.57 | +0.45 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BROX]] | -0.57 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[SNHG22]] | -0.55 | -0.30 / -0.60 | both halves | 2e-04 |  |
| [[RMND5A]] | -0.55 | -0.30 / -0.61 | both halves | 2e-04 | pathway: Aerobic respiration and respiratory electron transport |
| [[USF2]] | -0.50 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ATN1]] | -0.50 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[LINC02035]] | -0.50 | -0.23 / -0.50 | both halves | 5e-04 |  |
| [[CREBL2]] | -0.50 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[DVL3]] | -0.50 | -0.21 / -0.54 | both halves | 7e-04 |  |
| [[SRRM2]] | -0.49 | -0.25 / -0.47 | both halves | 4e-04 |  |
| [[FAM120AOS]] | -0.49 | -0.21 / -0.41 | both halves | 7e-04 |  |
| [[SORBS3]] | -0.49 | -0.40 / -0.37 | both halves | 7e-05 |  |
| [[DCTN1]] | -0.49 | -0.37 / -0.58 | both halves | 9e-05 | pathway: Organelle biogenesis and maintenance |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-50.0, -16.2); signed map (-38.1, -27.0). **Vector** length 56.7, 15.8% of its response variance represented; |z| ≥ 3 in 526 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Respiratory electron transport* (reactome, mean cos +0.51 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change | +2.0 | +3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.8 | +1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +2.8 |
|  | [[EX229 (drug)]] 0.5 µM |  | +1.4 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.4 | +3.5 |
|  | [[EX229 (drug)]] 5 µM |  | +1.3 | +1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.7 | +1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | -2.7 | +7.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.6 | -3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | -2.5 | +5.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ATP synthase membrane subunit c locus 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:48,892,765-48,895,871 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ATP5G, ATP5G1 |
| Gene groups (HGNC) | Mitochondrial complex V: ATP synthase subunits |
| Hallmark sets | MTORC1_SIGNALING, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 7 pathways, smallest: Formation of ATP by chemiosmotic coupling; Cristae formation; Mitochondrial protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [P05496](https://www.uniprot.org/uniprotkb/P05496) (ATP synthase F(0) complex subunit C1, mitochondrial):

> Subunit c, of the mitochondrial membrane ATP synthase complex (F(1)F(0) ATP synthase or Complex V) that produces ATP from ADP in the presence of a proton gradient across the membrane which is generated by electron transport complexes of the respiratory chain (Probable). ATP synthase complex consist of a soluble F(1) head domain - the catalytic core - and a membrane F(1) domain - the membrane proton channel. These two domains are linked by a central stalk rotating inside the F(1) region and a …

**Summary**, from NCBI Gene [516](https://www.ncbi.nlm.nih.gov/gene/516):

> This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic portion of mitochondrial ATP synthase consists of 5 different subunits (alpha, beta, gamma, …

**Accessions** — [HGNC:841](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:841) · Entrez [516](https://www.ncbi.nlm.nih.gov/gene/516) · UniProt [P05496](https://www.uniprot.org/uniprotkb/P05496) · Ensembl [ENSG00000159199](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159199)

## Data

Gene col 8226: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8226); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8226, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8226]; `tensor/DDL_lfc|DDL_z.npy` [8226]; `embed/gene_vectors.npy` [8226]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8226 or target_col == 8226). Every well: [[ATP5MC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP5MC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
