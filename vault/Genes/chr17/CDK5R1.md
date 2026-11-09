---
symbol: "CDK5R1"
type: "gene"
col: 10748
ensembl_id: "ENSG00000176749"
name: "cyclin dependent kinase 5 regulatory subunit 1"
location: "17q11.2"
module: 5
arm: "+"
pooled_cpm: 3.15
n_lines_expressing: 47
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# CDK5R1

*cyclin dependent kinase 5 regulatory subunit 1* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 4.80× (z +13.7, q 6e-40, up in 30 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Carbidopa (monohydrate) (drug)]] 0.5 µM in 1 line (HT-29 0.0592×; ⚠ unreliable plate only).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRR7-AS1]] (+0.58, fdr 1e-05), [[TMEM223]] (+0.56, fdr 2e-05), [[NKAIN1]] (+0.55, fdr 1e-05); moves opposite to [[ATF6B]] (-0.48, fdr 2e-05), [[CYLD]] (-0.45, fdr 6e-05), [[CAT]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10748.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **4.80×** | +13.7 | 6e-40 | 30/36 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.93×** | +13.3 | 1e-37 | 24/31 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.30×** | +10.3 | 2e-22 | 19/32 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.85×** | +8.8 | 2e-16 | 14/17 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.41×** | +7.4 | 2e-11 | 1/5 (A498) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.89×** | +5.6 | 3e-06 | 15/41 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.88×** | +5.5 | 3e-06 | 15/42 (SW 900, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.4 | 4e-06 | 10/41 (PANC-1, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +5.2 | 1e-05 | 11/41 (PANC-1, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.80×** | +5.1 | 2e-05 | 13/42 (NCI-H460, C32, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.81×** | +4.8 | 9e-05 | 0/5 | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +4.7 | 1e-04 | 12/43 (PANC-1, C32, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.67×** | +4.4 | 4e-04 | 15/40 (HT-29, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +4.1 | 0.001 | 11/30 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.61×** | +4.1 | 0.001 | 9/24 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.004 | 9/41 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Carbidopa (monohydrate) (drug)]] 0.5 µM in 1 line (HT-29 0.0592×; ⚠ unreliable plate only).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.61 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10748. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 3.05 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 17.5× (z +9.1) | [[Carbidopa (monohydrate) (drug)]] 0.5 µM 0.0592× (z -9.0) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.987 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.655 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.724 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10748), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR7-AS1]] | +0.58 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[TMEM223]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[NKAIN1]] | +0.55 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[SLC25A19]] | +0.53 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[NOP2]] | +0.51 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[NIP7]] | +0.50 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[POLR1G]] | +0.50 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[EEF1AKMT1]] | +0.50 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[IL12RB2]] | +0.50 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[NOP16]] | +0.50 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[AGO2]] | +0.50 | +0.52 / +0.33 | both halves | 1e-04 | pathway: Transcriptional Regulation by NPAS4 |
| [[NIPAL1]] | +0.50 | +0.48 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATF6B]] | -0.48 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[CYLD]] | -0.45 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[CAT]] | -0.45 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[DNAL1]] | -0.45 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[CHP1]] | -0.44 | -0.25 / -0.41 | both halves | 4e-04 |  |
| [[ATP6V1A]] | -0.44 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[EMC2]] | -0.44 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[ACSF2]] | -0.44 | -0.47 / -0.24 | both halves | 5e-04 |  |
| [[HINT3]] | -0.44 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[SLC50A1]] | -0.43 | -0.26 / -0.47 | both halves | 4e-04 |  |
| [[ERP29]] | -0.43 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[LRRFIP2]] | -0.43 | -0.50 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.456). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (28.4, -7.5); signed map (11.3, 18.5). **Vector** length 53.6, 7.44% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.4 | +13.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +13.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +10.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.0 | +8.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.3 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +3.9 |
|  | [[EX229 (drug)]] 5 µM |  | +1.5 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +0.2 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -1.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.5 | -1.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 5 regulatory subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:32,486,993-32,491,253 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p35nck5a, Nck5a, p35 |
| Gene groups (HGNC) | Cyclin dependent kinase 5 regulatory subunit family |
| Hallmark sets | HEDGEHOG_SIGNALING, COMPLEMENT, P53_PATHWAY |
| Reactome | 20 pathways, smallest: Activated NTRK2 signals through CDK5; CRMPs in Sema3A signaling; NPAS4 regulates expression of target genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15078](https://www.uniprot.org/uniprotkb/Q15078) (Cyclin-dependent kinase 5 activator 1):

> p35 is a neuron specific activator of CDK5. The complex p35/CDK5 is required for neurite outgrowth and cortical lamination. Involved in dendritic spine morphogenesis by mediating the EFNA1-EPHA4 signaling. Activator of TPKII. The complex p35/CDK5 participates in the regulation of the circadian clock by modulating the function of CLOCK protein: phosphorylates CLOCK at 'Thr-451' and 'Thr-461' and regulates the transcriptional activity of the CLOCK-BMAL1 heterodimer in association with altered …

**Summary**, from NCBI Gene [8851](https://www.ncbi.nlm.nih.gov/gene/8851):

> The protein encoded by this gene (p35) is a neuron-specific activator of cyclin-dependent kinase 5 (CDK5); the activation of CDK5 is required for proper development of the central nervous system. The p35 form of this protein is proteolytically cleaved by calpain, generating a p25 form. The cleavage of p35 into p25 results in relocalization of the protein from the cell periphery to nuclear and perinuclear regions. P25 deregulates CDK5 activity by prolonging its activation and changing its …

**Accessions** — [HGNC:1775](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1775) · Entrez [8851](https://www.ncbi.nlm.nih.gov/gene/8851) · UniProt [Q15078](https://www.uniprot.org/uniprotkb/Q15078) · Ensembl [ENSG00000176749](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176749)

## Data

Gene col 10748: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10748); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10748, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10748]; `tensor/DDL_lfc|DDL_z.npy` [10748]; `embed/gene_vectors.npy` [10748]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10748 or target_col == 10748). Every well: [[CDK5R1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK5R1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
