---
symbol: "SNAPC2"
type: "gene"
col: 2535
ensembl_id: "ENSG00000104976"
name: "small nuclear RNA activating complex polypeptide 2"
location: "19p13.2"
module: 3
arm: "+"
pooled_cpm: 6.1
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SNAPC2

*small nuclear RNA activating complex polypeptide 2* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.84× (z +5.9, q 2e-06, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.372× (z -5.1, q 2e-04, down in 19 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 0.219×, J82 0.274×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.103×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Sunitinib (drug)]] 5 µM in 1 line (C32 0.0797×; ⚠ toxic); [[Sinomenine (drug)]] 0.05 µM in 1 line (Hs 766T 0.0817×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CARD19]] (+0.75, fdr 7e-06), [[PLA2G15]] (+0.68, fdr 1e-05), [[MRPL43]] (+0.65, fdr 1e-05); moves opposite to [[SRSF1]] (-0.68, fdr 6e-05), [[EWSR1]] (-0.63, fdr 1e-04), [[ILF3]] (-0.62, fdr 4e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2535.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.84×** | +5.9 | 2e-06 | 28/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.78×** | +5.6 | 5e-06 | 21/32 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +5.5 | 5e-06 | 23/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.58×** | +4.3 | 0.003 | 3/11 (A-172, NCI-H2030, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.010 | 18/43 (KATO III, A549, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.7 | 0.022 | 4/48 (A-172, J82, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.051 | 16/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | 1.37× | +3.1 | 0.15 | 11/40 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2535.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 0.219×, J82 0.274×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.103×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Sunitinib (drug)]] 5 µM in 1 line (C32 0.0797×; ⚠ toxic); [[Sinomenine (drug)]] 0.05 µM in 1 line (Hs 766T 0.0817×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.372×** | -5.1 | 2e-04 | 19/44 (A-172, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.740×** | -4.2 | 0.008 | 15/45 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | 0.707× | -3.3 | 0.20 | 18/42 (SW 900, NCI-H1792, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.793× | -3.2 | 0.22 | 14/48 (SW480, SHP-77, …) | inconsistent across doses |  |
| [[Tadalafil (drug)]] 5 µM |  | 0.722× | -3.1 | 0.24 | 12/44 (NCI-H2347, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2535. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 7.49 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0948× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 7.88 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0797× (z -9.7) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 5.59 | 0 | 1 | — | [[Sinomenine (drug)]] 0.05 µM 0.0817× (z -9.0) |
| [[J82 (line)]] | alt | 7.30 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 6.01 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2535), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARD19]] | +0.75 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[PLA2G15]] | +0.68 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[MRPL43]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[LIN7B]] | +0.65 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[CIAO2B]] | +0.65 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[RRAS]] | +0.65 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[FAM89B]] | +0.63 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[MPG]] | +0.63 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[RPP21]] | +0.63 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[TPRG1L]] | +0.62 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[PMM1]] | +0.62 | +0.37 / +0.62 | both halves | 8e-05 |  |
| [[AGPAT2]] | +0.62 | +0.48 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF1]] | -0.68 | -0.39 / -0.68 | both halves | 6e-05 |  |
| [[EWSR1]] | -0.63 | -0.33 / -0.68 | both halves | 1e-04 |  |
| [[ILF3]] | -0.62 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[HMGN1]] | -0.61 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[HNRNPA3]] | -0.61 | -0.39 / -0.68 | both halves | 5e-05 |  |
| [[FUBP1]] | -0.60 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[ARGLU1]] | -0.58 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[DHFR]] | -0.58 | -0.16 / -0.70 | ⚠ one half (not replicated) | 0.001 |  |
| [[HNRNPA2B1]] | -0.57 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[GALC]] | -0.57 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[ENOSF1]] | -0.57 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[ACADM]] | -0.56 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[HNRNPU]] | -0.56 | -0.40 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SNAPC2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.691). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-34.6, 25.7); signed map (-29.1, 16.7). **Vector** length 60.3, 9.54% of its response variance represented; |z| ≥ 3 in 714 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +5.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.6 | +5.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.5 | +1.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.1 | +2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.0 | +0.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.4 | +0.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -3.4 | +4.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.5 | -5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.9 | -4.2 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | +1.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear RNA activating complex polypeptide 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:7,920,338-7,923,250 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SNAP45, PTFdelta |
| Gene groups (HGNC) | SNAP complex |
| Reactome | 5 pathways, smallest: RNA Polymerase III Transcription Initiation From Type 3 Promoter; RNA Polymerase III Transcription Initiation; RNA Polymerase III Abortive And Retractive Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13487](https://www.uniprot.org/uniprotkb/Q13487) (snRNA-activating protein complex subunit 2):

> Part of the SNAPc complex required for the transcription of both RNA polymerase II and III small-nuclear RNA genes. Binds to the proximal sequence element (PSE), a non-TATA-box basal promoter element common to these 2 types of genes. Recruits TBP and BRF2 to the U6 snRNA TATA box.

**Summary**, from NCBI Gene [6618](https://www.ncbi.nlm.nih.gov/gene/6618):

> This gene encodes a subunit of the snRNA-activating protein complex which is associated with the TATA box-binding protein. The encoded protein is necessary for RNA polymerase II and III dependent small-nuclear RNA gene transcription. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:11135](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11135) · Entrez [6618](https://www.ncbi.nlm.nih.gov/gene/6618) · UniProt [Q13487](https://www.uniprot.org/uniprotkb/Q13487) · Ensembl [ENSG00000104976](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104976)

## Data

Gene col 2535: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2535); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2535, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2535]; `tensor/DDL_lfc|DDL_z.npy` [2535]; `embed/gene_vectors.npy` [2535]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2535 or target_col == 2535). Every well: [[SNAPC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNAPC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
