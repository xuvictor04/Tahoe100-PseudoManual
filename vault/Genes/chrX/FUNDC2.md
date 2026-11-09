---
symbol: "FUNDC2"
type: "gene"
col: 9182
ensembl_id: "ENSG00000165775"
name: "FUN14 domain containing 2"
location: "Xq28"
module: 20
arm: "+"
pooled_cpm: 12.95
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# FUNDC2

*FUN14 domain containing 2* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.42× (z +11.3, q 1e-26, up in 44 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.155×; ⚠ cell-cycle shift, explains ~0% of this change); [[Omeprazole (drug)]] 0.5 µM in 1 line (BT-474 0.0878×).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTC1]] (+0.62, fdr 1e-05), [[DHFR]] (+0.61, fdr 2e-05), [[PCMTD2]] (+0.61, fdr 6e-05); moves opposite to [[TRIM11]] (-0.50, fdr 5e-04), [[MRPL46]] (-0.49, fdr 4e-05), [[WAPL]] (-0.47, fdr 1e-04).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9182.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.42×** | +11.3 | 1e-26 | 44/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.90×** | +8.2 | 4e-14 | 40/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +8.2 | 4e-14 | 24/30 (SW480, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +8.0 | 2e-13 | 32/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.78×** | +7.4 | 2e-11 | 34/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.92×** | +7.2 | 7e-11 | 33/44 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.88×** | +7.1 | 1e-10 | 35/48 (AsPC-1, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +7.0 | 1e-10 | 24/36 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.43×** | +6.4 | 8e-09 | 24/46 (HT-29, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +6.2 | 4e-08 | 24/40 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +6.0 | 1e-07 | 24/48 (HT-29, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +5.2 | 9e-06 | 14/24 (A-172, HT-29, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Acetohexamide (drug)]] 0.5 µM |  | **1.47×** | +4.9 | 4e-05 | 23/46 (HT-29, SW1417, …) | inconsistent across doses | position effect removed |
| [[Pasireotide (acetate) (drug)]] 0.5 µM |  | **1.40×** | +4.3 | 6e-04 | 22/47 (NCI-H2347, SW480, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.37×** | +3.9 | 0.004 | 13/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.010 | 15/47 (HT-29, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.049 | 11/47 (MIA PaCa-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9182.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.155×; ⚠ cell-cycle shift, explains ~0% of this change); [[Omeprazole (drug)]] 0.5 µM in 1 line (BT-474 0.0878×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.764× | -3.4 | 0.33 | 11/47 (NCI-H2347, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.771× | -3.2 | 0.33 | 9/47 (KATO III, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9182. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.2 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.57× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 16.3 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.79× (z +11.4) | — |
| [[AsPC-1 (line)]] | alt | 25.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.20× (z +9.4) | — |
| [[BT-474 (line)]] | alt | 7.47 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0878× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9182), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTC1]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[DHFR]] | +0.61 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[PCMTD2]] | +0.61 | +0.38 / +0.68 | both halves | 6e-05 |  |
| [[PHOSPHO2]] | +0.59 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[RPL10]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[EEF1A1P5]] | +0.58 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[RPS3A]] | +0.57 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[CREG1]] | +0.56 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[RPS18]] | +0.56 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[MORF4L1]] | +0.55 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[BBS2]] | +0.55 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[EEF1A1]] | +0.55 | +0.44 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM11]] | -0.50 | -0.23 / -0.55 | both halves | 5e-04 |  |
| [[MRPL46]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[WAPL]] | -0.47 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[CCDC137]] | -0.45 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[UBE2J2]] | -0.45 | -0.45 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.451). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-27.9, -26.0); signed map (-24.8, -34.2). **Vector** length 59.7, 8.97% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.53 to 10); *Peptide chain elongation* (reactome, mean cos +0.52 to 9); *PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA* (reactome, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +7.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.6 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.3 | +1.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +1.2 | -0.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -0.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | -1.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +2.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | FUN14 domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:155,025,980-155,060,304 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HCBP6, DC44 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWH2](https://www.uniprot.org/uniprotkb/Q9BWH2) (FUN14 domain-containing protein 2):

> Binds directly and specifically 1,2-Diacyl-sn-glycero-3-phospho-(1'-myo-inositol-3',4',5'-bisphosphate) (PIP3) leading to the recruitment of PIP3 to mitochondria and may play a role in the regulation of the platelet activation via AKT/GSK3B/cGMP signaling pathways. May act as transcription factor that regulates SREBP1 (isoform SREBP-1C) expression in order to modulate triglyceride (TG) homeostasis in hepatocytes.

**Summary**, from NCBI Gene [65991](https://www.ncbi.nlm.nih.gov/gene/65991):

> Enables phosphatidylinositol-3,4,5-trisphosphate binding activity. Involved in intracellular triglyceride homeostasis. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24925](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24925) · Entrez [65991](https://www.ncbi.nlm.nih.gov/gene/65991) · UniProt [Q9BWH2](https://www.uniprot.org/uniprotkb/Q9BWH2) · Ensembl [ENSG00000165775](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165775)

## Data

Gene col 9182: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9182); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9182, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9182]; `tensor/DDL_lfc|DDL_z.npy` [9182]; `embed/gene_vectors.npy` [9182]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9182 or target_col == 9182). Every well: [[FUNDC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FUNDC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
