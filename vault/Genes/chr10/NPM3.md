---
symbol: "NPM3"
type: "gene"
col: 2887
ensembl_id: "ENSG00000107833"
name: "nucleophosmin/nucleoplasmin 3"
location: "10q24.32"
module: 33
arm: "+"
pooled_cpm: 13.06
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# NPM3

*nucleophosmin/nucleoplasmin 3* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.01× (z +7.9, q 2e-12, up in 36 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change. The strongest without an alert is [[EX229 (drug)]] 5 µM: 2.57× (z +3.5, q 0.031, up in 23 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.628× (z -4.7, q 0.002, down in 26 of 44 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C20orf27]] (+0.72, fdr 7e-06), [[NARS2]] (+0.71, fdr 1e-05), [[NLE1]] (+0.69, fdr 1e-05); moves opposite to [[UBE2A]] (-0.67, fdr 5e-05), [[CHD3]] (-0.63, fdr 7e-05), [[C11orf58]] (-0.60, fdr 8e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 10 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2887.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **3.01×** | +7.9 | 2e-12 | 36/38 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **2.62×** | +6.6 | 1e-08 | 14/21 (HT-29, A498, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.41×** | +6.1 | 3e-07 | 29/38 (KATO III, PANC-1, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **2.05×** | +4.7 | 3e-04 | 20/26 (HepG2/C3A, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.70×** | +3.8 | 0.018 | 27/47 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **1.71×** | +3.7 | 0.021 | 24/40 (C32, NCI-H1792, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **2.57×** | +3.5 | 0.031 | 23/42 (NCI-H1573, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **1.64×** | +3.5 | 0.031 | 19/39 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.61×** | +3.4 | 0.039 | 24/46 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.60×** | +3.4 | 0.042 | 22/46 (A-172, NCI-H1792, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.2 | 0.068 | 22/45 (A-172, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2887.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.628×** | -4.7 | 0.002 | 26/44 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.336×** | -4.1 | 0.014 | 33/46 (KATO III, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.566×** | -3.9 | 0.019 | 29/45 (C32, C-33 A, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.688×** | -3.6 | 0.042 | 26/46 (COLO 205, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.739× | -3.0 | 0.21 | 25/46 (LOX-IMVI, A-427, …) | rises with dose | low cells (technical?); position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.626× | -3.0 | 0.21 | 18/47 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | 0.445× | -3.0 | 0.21 | 19/46 (LS 180, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2887. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 23.4 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 6.91 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0785× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 12.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.264× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 16.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -10.5) |
| [[A-172 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2887), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C20orf27]] | +0.72 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[NARS2]] | +0.71 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[NLE1]] | +0.69 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[NAA10]] ⚠ | +0.68 | +0.48 / +0.67 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM147]] | +0.67 | +0.50 / +0.74 | both halves | 1e-05 |  |
| [[WDR3]] | +0.66 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[GGCT]] | +0.66 | +0.69 / +0.42 | both halves | 4e-05 |  |
| [[POLR1B]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[BOP1]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 | STRING 438 |
| [[MRPS26]] | +0.64 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[PDCD11]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ANKS6]] | +0.64 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[MRPL12]] | +0.63 | +0.38 / +0.66 | both halves | 7e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2A]] | -0.67 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[CHD3]] | -0.63 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[C11orf58]] | -0.60 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[TMEM202-AS1]] | -0.58 | -0.44 / -0.27 | both halves | 3e-04 |  |
| [[SUCLG2-DT]] | -0.57 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[HCG27]] | -0.57 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[HMGN2]] | -0.56 | -0.26 / -0.49 | both halves | 4e-04 |  |
| [[MMADHC-DT]] | -0.56 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[DAZAP2]] | -0.55 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[GNAS]] | -0.55 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[CYB5D2]] | -0.55 | -0.37 / -0.38 | both halves | 9e-05 |  |
| [[PLA2G6]] | -0.54 | -0.44 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.707). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.6, -43.0); signed map (-7.8, -50.6). **Vector** length 66.1, 15.0% of its response variance represented; |z| ≥ 3 in 650 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.52 to 8); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.55 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.55 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | +3.1 | +3.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +2.6 | +3.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +3.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.8 | +1.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.3 | -3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.4 | -1.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | nucleophosmin/nucleoplasmin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:101,781,325-101,783,446 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [O75607](https://www.uniprot.org/uniprotkb/O75607) (Nucleoplasmin-3):

> Plays a role in the regulation of diverse cellular processes such as ribosome biogenesis, chromatin remodeling or protein chaperoning. Modulates the histone chaperone function and the RNA-binding activity of nucleolar phosphoprotein B23/NPM. Efficiently mediates chromatin remodeling when included in a pentamer containing NPM3 and NPM.

**Summary**, from NCBI Gene [10360](https://www.ncbi.nlm.nih.gov/gene/10360):

> The protein encoded by this gene is related to the nuclear chaperone phosphoproteins, nucleoplasmin and nucleophosmin. This protein is strongly expressed in diverse cell types where it localizes primarily to the nucleus. Based on its similarity to nucleoplasmin and nucleophosmin, this protein likely functions as a molecular chaperone in the cell nucleus. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:7931](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7931) · Entrez [10360](https://www.ncbi.nlm.nih.gov/gene/10360) · UniProt [O75607](https://www.uniprot.org/uniprotkb/O75607) · Ensembl [ENSG00000107833](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107833)

## Data

Gene col 2887: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2887); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2887, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2887]; `tensor/DDL_lfc|DDL_z.npy` [2887]; `embed/gene_vectors.npy` [2887]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2887 or target_col == 2887). Every well: [[NPM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
