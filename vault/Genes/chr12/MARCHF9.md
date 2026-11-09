---
symbol: "MARCHF9"
type: "gene"
col: 6285
ensembl_id: "ENSG00000139266"
name: "membrane associated ring-CH-type finger 9"
location: "12q14.1"
module: 25
arm: "-"
pooled_cpm: 7.4
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# MARCHF9

*membrane associated ring-CH-type finger 9* — 12q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.73× (z +4.7, q 0.001, up in 24 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.391× (z -8.0, q 5e-13, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACAP1]] (+0.76, fdr 7e-06), [[ARID3A]] (+0.74, fdr 1e-05), [[DCTN6-DT]] (+0.68, fdr 3e-05); moves opposite to [[PSME3]] (-0.74, fdr 1e-05), [[MOB1A]] (-0.72, fdr 7e-06), [[LIN7C]] (-0.67, fdr 1e-05).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6285.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.73×** | +4.7 | 0.001 | 24/42 (PANC-1, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.68×** | +4.4 | 0.003 | 20/39 (PANC-1, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.037 | 17/46 (NCI-H1792, PANC-1, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.46× | +3.2 | 0.17 | 14/46 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | 1.44× | +3.1 | 0.20 | 14/45 (SNU-423, CFPAC-1, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.43× | +3.1 | 0.20 | 14/41 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.43× | +3.0 | 0.20 | 15/36 (HOP62, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6285.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.391×** | -8.0 | 5e-13 | 35/46 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.399×** | -7.9 | 9e-13 | 35/45 (C-33 A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~2% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.595×** | -6.3 | 6e-08 | 23/43 (LoVo, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.511×** | -5.7 | 1e-06 | 27/43 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.533×** | -5.4 | 8e-06 | 24/45 (COLO 205, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.539×** | -5.3 | 1e-05 | 25/44 (NCI-H1792, A549, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.555×** | -4.8 | 1e-04 | 22/41 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.598×** | -4.4 | 7e-04 | 21/45 (hTERT-HPNE, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.636×** | -3.9 | 0.006 | 22/39 (SHP-77, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~8% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.346×** | -3.8 | 0.009 | 17/42 (CFPAC-1, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.599×** | -3.6 | 0.015 | 17/46 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.659×** | -3.6 | 0.016 | 18/44 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.661×** | -3.4 | 0.028 | 20/44 (NCI-H2347, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.690×** | -3.2 | 0.058 | 18/40 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.704×** | -3.0 | 0.096 | 13/47 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6285. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 18.3 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0671× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0845× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 5.96 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.132× (z -9.5) |
| [[C-33 A (line)]] | alt | 9.00 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0448× (z -10.6) |
| [[LoVo (line)]] | wt | 8.80 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.212× (z -8.5) |
| [[SHP-77 (line)]] | alt | 7.81 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6285), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACAP1]] | +0.76 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[ARID3A]] | +0.74 | +0.49 / +0.79 | both halves | 1e-05 |  |
| [[DCTN6-DT]] | +0.68 | +0.45 / +0.74 | both halves | 3e-05 |  |
| [[COMMD6]] | +0.67 | +0.42 / +0.78 | both halves | 4e-05 |  |
| [[SMIM26]] ⚠ | +0.66 | +0.49 / +0.69 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[UBE2B]] | +0.66 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[GGT7]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[AFTPH]] | +0.63 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[SNHG19]] | +0.63 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[RPL18]] ⚠ | +0.63 | +0.37 / +0.71 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TSTD1]] | +0.63 | +0.39 / +0.65 | both halves | 5e-05 |  |
| [[IFI27L2]] | +0.63 | +0.39 / +0.69 | both halves | 6e-05 |  |
| [[CDKN2D]] | +0.63 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[PITPNA-AS1]] | +0.63 | +0.49 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.74 | -0.54 / -0.77 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.72 | -0.60 / -0.69 | both halves | 7e-06 |  |
| [[LIN7C]] | -0.67 | -0.49 / -0.72 | both halves | 1e-05 | STRING 427 |
| [[TARDBP]] | -0.66 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[CAPRIN1]] | -0.66 | -0.47 / -0.69 | both halves | 2e-05 |  |
| [[ZNF236]] | -0.65 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[RCN1]] | -0.64 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[ABCF2]] | -0.63 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[CCT7]] | -0.62 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[EWSR1]] | -0.62 | -0.37 / -0.65 | both halves | 7e-05 |  |
| [[ELK4]] | -0.62 | -0.37 / -0.63 | both halves | 8e-05 |  |
| [[XRCC5]] | -0.62 | -0.45 / -0.64 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-32.3, -26.3); signed map (-27.8, 14.1). **Vector** length 63.6, 11.9% of its response variance represented; |z| ≥ 3 in 747 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +3.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.3 | +4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.5 | +3.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.3 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +0.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.6 | +2.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.5 | +2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.5 | +0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -2.2 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -1.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | membrane associated ring-CH-type finger 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.1 — chr12:57,755,103-57,760,411 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RNF179, FLJ36578; previously MARCH9 |
| Gene groups (HGNC) | Ring finger proteins; Membrane associated ring-CH-type fingers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YJ5](https://www.uniprot.org/uniprotkb/Q86YJ5) (E3 ubiquitin-protein ligase MARCHF9):

> E3 ubiquitin-protein ligase that may mediate ubiquitination of MHC-I, CD4 and ICAM1, and promote their subsequent endocytosis and sorting to lysosomes via multivesicular bodies. E3 ubiquitin ligases accept ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfer the ubiquitin to targeted substrates.

**Summary**, from NCBI Gene [92979](https://www.ncbi.nlm.nih.gov/gene/92979):

> MARCH9 is a member of the MARCH family of membrane-bound E3 ubiquitin ligases (EC 6.3.2.19). MARCH enzymes add ubiquitin (see MIM 191339) to target lysines in substrate proteins, thereby signaling their vesicular transport between membrane compartments. MARCH9 induces internalization of several membrane glycoproteins and directs them to the endosomal compartment (Bartee et al., 2004 [PubMed 14722266]; Hoer et al., 2007 [PubMed 17174307]).[supplied by OMIM, Apr 2010]

**Accessions** — [HGNC:25139](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25139) · Entrez [92979](https://www.ncbi.nlm.nih.gov/gene/92979) · UniProt [Q86YJ5](https://www.uniprot.org/uniprotkb/Q86YJ5) · Ensembl [ENSG00000139266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139266)

## Data

Gene col 6285: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6285); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6285, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6285]; `tensor/DDL_lfc|DDL_z.npy` [6285]; `embed/gene_vectors.npy` [6285]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6285 or target_col == 6285). Every well: [[MARCHF9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MARCHF9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
