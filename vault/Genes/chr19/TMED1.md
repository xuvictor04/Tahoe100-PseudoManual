---
symbol: "TMED1"
type: "gene"
col: 1781
ensembl_id: "ENSG00000099203"
name: "transmembrane p24 trafficking protein 1"
location: "19p13.2"
module: 48
arm: "+"
pooled_cpm: 5.6
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# TMED1

*transmembrane p24 trafficking protein 1* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.00× (z +6.4, q 1e-07, up in 18 of 27 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.524× (z -8.4, q 4e-14, down in 32 of 41 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2G]] (+0.62, fdr 1e-05, ⚠ POLR2G in the vector space only through flagged drug-doses), [[B9D2]] (+0.57, fdr 1e-05), [[MFSD5]] (+0.57, fdr 2e-05), [[ATP6V0B]] (+0.54, fdr 3e-05); moves opposite to [[NPM1]] (-0.47, fdr 3e-05), [[DTD1]] (-0.46, fdr 2e-04), [[CDH4]] (-0.44, fdr 1e-04).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1781.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.00×** | +6.4 | 1e-07 | 18/27 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +6.0 | 6e-07 | 6/8 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.66×** | +4.6 | 5e-04 | 12/31 (HEC-1-A, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +4.6 | 5e-04 | 6/16 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.4 | 0.001 | 14/31 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.46×** | +3.5 | 0.052 | 12/41 (NCI-H2030, LOX-IMVI, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1781.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.524×** | -8.4 | 4e-14 | 32/41 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.464×** | -7.0 | 6e-10 | 32/47 (SW480, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.481×** | -6.7 | 4e-09 | 30/47 (NCI-H2347, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.485×** | -6.6 | 5e-09 | 31/47 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.515×** | -6.1 | 1e-07 | 25/46 (LOX-IMVI, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.360×** | -4.9 | 1e-04 | 23/46 (NCI-H1792, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.592×** | -4.8 | 1e-04 | 19/39 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.626×** | -4.3 | 0.001 | 22/40 (HEC-1-A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.748×** | -3.7 | 0.011 | 18/48 (C32, H4, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.480×** | -3.5 | 0.027 | 14/44 (LoVo, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.504×** | -3.3 | 0.057 | 13/39 (BT-474, SHP-77, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.703×** | -3.1 | 0.084 | 15/44 (HS-578T, NCI-H460, …) | top dose only |  |
| [[DTP3 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.712×** | -3.1 | 0.084 | 5/47 (A498, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1781. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 12.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -13.2) |
| [[MIA PaCa-2 (line)]] | alt | 5.23 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Retinoic acid (drug)]] 5 µM 0.215× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 4.93 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -9.2) |
| [[BT-474 (line)]] | alt | 8.45 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.109× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 7.56 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 9.40 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -9.2) |
| [[SNU-423 (line)]] | alt | 6.55 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -9.4) |
| [[A-172 (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1781), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 16 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2G]] ⚠ | +0.62 | +0.63 / +0.57 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[B9D2]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[MFSD5]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[ATP6V0B]] | +0.54 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[NDUFB11]] ⚠ | +0.54 | +0.44 / +0.50 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZDHHC12]] | +0.52 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[TM9SF1]] | +0.52 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[COPS9]] | +0.52 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[SCAMP2]] | +0.51 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[HIGD2A]] | +0.51 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[UQCR10]] ⚠ | +0.50 | +0.42 / +0.52 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[UXT]] | +0.50 | +0.39 / +0.48 | both halves | 6e-05 |  |
| [[RABAC1]] | +0.49 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[CCDC142]] | +0.49 | +0.32 / +0.56 | both halves | 1e-04 |  |
| [[QRICH1]] | +0.49 | +0.38 / +0.51 | both halves | 6e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPM1]] | -0.47 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[DTD1]] | -0.46 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[CDH4]] | -0.44 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[ITPR3]] | -0.44 | -0.17 / -0.49 | ⚠ not reproduced | 0.001 |  |
| [[RASSF3]] | -0.43 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[AMPD3]] | -0.43 | -0.48 / -0.27 | both halves | 3e-04 |  |
| [[DDX21]] | -0.41 | -0.41 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.452). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-50.5, -22.0); signed map (-38.2, 10.7). **Vector** length 47.7, 6.41% of its response variance represented; |z| ≥ 3 in 766 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +2.3 | +3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +0.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.1 | +2.1 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.0 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.9 | +2.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +0.9 | +1.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -2.0 | -4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.8 | -7.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.7 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane p24 trafficking protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,832,067-10,836,318 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ST2L, MGC1270, IL1RL1LG, Il1rl1l, p24gamma1, p24g1 |
| Gene groups (HGNC) | Transmembrane p24 trafficking proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13445](https://www.uniprot.org/uniprotkb/Q13445) (Transmembrane emp24 domain-containing protein 1):

> Potential role in vesicular protein trafficking, mainly in the early secretory pathway. May act as a cargo receptor at the lumenal side for incorporation of secretory cargo molecules into transport vesicles and may be involved in vesicle coat formation at the cytoplasmic side. Plays a positive role in IL-33-mediated IL-8 and IL-6 production by interacting with interleukin-33 receptor IL1RL1. Also plays a role in the modulation of innate immune signaling through the cGAS-STING pathway by …

**Summary**, from NCBI Gene [11018](https://www.ncbi.nlm.nih.gov/gene/11018):

> This gene belongs to the TMED (transmembrane emp24 domain-containing) protein family, which is involved in the vesicular trafficking of proteins. The protein encoded by this gene was identified by its interaction with interleukin 1 receptor-like 1 (IL1RL1) and may play a role in innate immunity. This protein lacks any similarity to other interleukin 1 ligands. Alternative splicing results in multiple transcript variants of this gene. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:17291](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17291) · Entrez [11018](https://www.ncbi.nlm.nih.gov/gene/11018) · UniProt [Q13445](https://www.uniprot.org/uniprotkb/Q13445) · Ensembl [ENSG00000099203](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099203)

## Data

Gene col 1781: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1781); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1781, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1781]; `tensor/DDL_lfc|DDL_z.npy` [1781]; `embed/gene_vectors.npy` [1781]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1781 or target_col == 1781). Every well: [[TMED1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMED1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
