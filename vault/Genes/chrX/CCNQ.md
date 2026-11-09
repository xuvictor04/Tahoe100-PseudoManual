---
symbol: "CCNQ"
type: "gene"
col: 15398
ensembl_id: "ENSG00000262919"
name: "cyclin Q"
location: "Xq28"
module: 3
arm: "+"
pooled_cpm: 4.39
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CCNQ

*cyclin Q* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.22× (z +7.5, q 5e-11, up in 33 of 45 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.89× (z +4.1, q 0.003, up in 10 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (KATO III 0.0583×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.258×; ⚠ cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 5 µM in 1 line (NCI-H460 0.257×; ⚠ cell-cycle shift, explains ~97% of this change); [[Hesperidin (drug)]] 5 µM in 1 line (NCI-H1573 0.0728×); [[IQ 1 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0661×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMYND19]] (+0.69, fdr 1e-05), [[ZXDC]] (+0.69, fdr 2e-05), [[MRPL41]] (+0.69, fdr 3e-05, ⚠ MRPL41 in the vector space only through flagged drug-doses), [[PUSL1]] (+0.68, fdr 1e-05); moves opposite to [[CHD3]] (-0.61, fdr 6e-05), [[ZSCAN30]] (-0.60, fdr 5e-05), [[DDX39B]] (-0.57, fdr 6e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15398.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.22×** | +7.5 | 5e-11 | 33/45 (SW1417, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.12×** | +7.0 | 6e-10 | 30/46 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.07×** | +6.8 | 2e-09 | 24/45 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +5.7 | 1e-06 | 15/27 (SW1417, NCI-H23, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +4.9 | 1e-04 | 9/25 (J82, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.89×** | +4.1 | 0.003 | 10/31 (Hs 766T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **1.54×** | +4.0 | 0.005 | 5/23 (CFPAC-1, HT-29, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.54×** | +3.8 | 0.008 | 1/9 (SNU-423) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.46×** | +3.5 | 0.029 | 7/32 (LS 180, MIA PaCa-2, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +3.3 | 0.065 | 3/13 (A498, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.46×** | +3.2 | 0.073 | 7/36 (NCI-H23, NCI-H2347, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.42×** | +3.2 | 0.073 | 11/30 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.26×** | +3.0 | 0.100 | 12/36 (HT-29, SW480, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.60×** | +3.0 | 0.100 | 6/36 (NCI-H23, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15398.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (KATO III 0.0583×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.258×; ⚠ cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 5 µM in 1 line (NCI-H460 0.257×; ⚠ cell-cycle shift, explains ~97% of this change); [[Hesperidin (drug)]] 5 µM in 1 line (NCI-H1573 0.0728×); [[IQ 1 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0661×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | 0.539× | -3.0 | 0.85 | 11/42 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15398. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 7.96 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 4.91 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0583× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 4.23 | 0 | 1 | — | [[IQ 1 (drug)]] 0.05 µM 0.0661× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 3.54 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0728× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 4.48 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.257× (z -8.6) ⚠ cell-cycle shift, explains ~97% of this change |
| [[A-427 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.403 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15398), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND19]] | +0.69 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[ZXDC]] | +0.69 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[MRPL41]] ⚠ | +0.69 | +0.43 / +0.68 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PUSL1]] | +0.68 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[CDC34]] | +0.68 | +0.46 / +0.67 | both halves | 2e-05 |  |
| [[NUBP2]] | +0.67 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[FANCE]] | +0.66 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[MIIP]] | +0.66 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[DEXI]] | +0.65 | +0.45 / +0.74 | both halves | 3e-05 |  |
| [[RTL10]] | +0.65 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[MPG]] | +0.65 | +0.28 / +0.68 | both halves | 3e-04 |  |
| [[SELENOO]] | +0.65 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[TRAPPC4]] | +0.65 | +0.42 / +0.64 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHD3]] | -0.61 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[ZSCAN30]] | -0.60 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[DDX39B]] | -0.57 | -0.22 / -0.58 | both halves | 6e-04 |  |
| [[ACADM]] | -0.57 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[PAPOLA]] | -0.56 | -0.29 / -0.56 | both halves | 3e-04 |  |
| [[RIPK2-DT]] | -0.55 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[IFT80]] | -0.55 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[DZIP3]] | -0.55 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[HNRNPU]] | -0.54 | -0.23 / -0.51 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.666). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-5.2, -19.1); signed map (-40.6, -2.2). **Vector** length 50.1, 6.81% of its response variance represented; |z| ≥ 3 in 793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.2 | +7.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.0 | +7.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.7 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.1 | +5.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.0 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +3.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | cyclin Q |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:153,587,925-153,600,045 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CycM; previously FAM58A |
| Gene groups (HGNC) | Cyclins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N1B3](https://www.uniprot.org/uniprotkb/Q8N1B3) (Cyclin-Q):

> Activating cyclin for the cyclin-associated kinase CDK10.

**Summary**, from NCBI Gene [92002](https://www.ncbi.nlm.nih.gov/gene/92002):

> Mutations in this gene have been shown to cause an X-linked dominant STAR syndrome that typically manifests syndactyly, telecanthus and anogenital and renal malformations. The protein encoded by this gene contains a cyclin-box-fold domain which suggests it may have a role in controlling nuclear cell division cycles. Alternative splicing results in multiple transcript variants encoding distinct isoforms. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:28434](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28434) · Entrez [92002](https://www.ncbi.nlm.nih.gov/gene/92002) · UniProt [Q8N1B3](https://www.uniprot.org/uniprotkb/Q8N1B3) · Ensembl [ENSG00000262919](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000262919)

## Data

Gene col 15398: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15398); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15398, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15398]; `tensor/DDL_lfc|DDL_z.npy` [15398]; `embed/gene_vectors.npy` [15398]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15398 or target_col == 15398). Every well: [[CCNQ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNQ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
