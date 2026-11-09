---
symbol: "CTC1"
type: "gene"
col: 10981
ensembl_id: "ENSG00000178971"
name: "CST telomere replication complex component 1"
location: "17p13.1"
module: 20
arm: "+"
pooled_cpm: 10.93
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 5
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# CTC1

*CST telomere replication complex component 1* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.99× (z +15.8, q 0e+00, up in 20 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 1.52× (z +4.3, q 0.002, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.727× (z -4.6, q 0.003, down in 23 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMG1P1]] (+0.67, fdr 7e-06), [[CPSF6]] (+0.66, fdr 1e-05), [[CIZ1]] (+0.64, fdr 1e-05); moves opposite to [[RBBP6]] (-0.66, fdr 7e-06), [[SON]] (-0.63, fdr 7e-06), [[PDCD7]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10981.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.99×** | +15.8 | 0e+00 | 20/20 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.62×** | +15.6 | 0e+00 | 33/35 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.33×** | +11.4 | 1e-27 | 20/26 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.6 | 7e-04 | 23/41 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +4.4 | 0.001 | 21/46 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +4.3 | 0.002 | 23/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +4.2 | 0.002 | 22/47 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.016 | 13/47 (SHP-77, CFPAC-1, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10981.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.727×** | -4.6 | 0.003 | 23/46 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.674×** | -4.0 | 0.017 | 17/46 (COLO 205, NCI-H661, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.670×** | -3.9 | 0.017 | 19/46 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.771×** | -3.7 | 0.028 | 23/48 (Hs 766T, Panc 03.27, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.697×** | -3.7 | 0.028 | 15/47 (SW48, H4, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.738× | -3.1 | 0.19 | 10/47 (Hs 766T, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10981. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.4 | 7 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 8.74× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 6.34× (z +11.4) | [[Ritonavir (drug)]] 0.5 µM 0.206× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 12.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.2× (z +12.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 6.56 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 17.7× (z +12.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 14.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.51× (z +10.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -9.5) |
| [[A-172 (line)]] | wt | 7.93 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0516× (z -13.0) |
| [[A498 (line)]] | wt | 13.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.75× (z +9.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 8.54 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.40× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 18.3 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0953× (z -13.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -12.9) |
| [[PANC-1 (line)]] | alt | 9.88 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.31× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 18.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.96× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 18.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.89× (z +8.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 7.30 | 0 | 1 | — | [[Sinomenine (drug)]] 0.05 µM 0.0805× (z -10.0) |
| [[KATO III (line)]] | alt | 8.16 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.2× (z +11.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 6.45 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.6× (z +12.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 7.72 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.95× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 6.14 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0586× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 16.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.80× (z +9.9) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 7.81 | 0 | 1 | — | [[Furosemide (drug)]] 0.5 µM 0.0907× (z -8.7) |
| [[SHP-77 (line)]] | alt | 23.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 11.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.95× (z +8.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10981), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG1P1]] | +0.67 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[CPSF6]] | +0.66 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[CIZ1]] | +0.64 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[NPEPPSP1]] | +0.63 | +0.57 / +0.67 | both halves | 8e-06 |  |
| [[LENG8]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[FUNDC2]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[ZC3H3]] | +0.62 | +0.31 / +0.72 | both halves | 2e-04 |  |
| [[SUMO1]] | +0.61 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[DHFR]] | +0.61 | +0.34 / +0.70 | both halves | 1e-04 |  |
| [[PABIR2]] | +0.60 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[HDAC1]] | +0.60 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[KCTD2]] | +0.59 | +0.28 / +0.63 | both halves | 3e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP6]] | -0.66 | -0.66 / -0.68 | both halves | 7e-06 |  |
| [[SON]] | -0.63 | -0.75 / -0.59 | both halves | 7e-06 |  |
| [[PDCD7]] | -0.62 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[C14orf119]] | -0.61 | -0.57 / -0.63 | both halves | 9e-06 |  |
| [[DDX24]] | -0.61 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[SIX1]] | -0.59 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[FADD]] | -0.59 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[CEBPZ]] | -0.58 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[CCDC137]] | -0.57 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[FAM32A]] | -0.57 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[PPP1R12A]] | -0.56 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[EID2]] | -0.54 | -0.55 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.483). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-27.4, -26.7); signed map (-26.3, -34.1). **Vector** length 93.5, 19.9% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +11.3 | +15.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.9 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.6 | +11.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.0 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +3.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -1.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | +0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -1.4 |
|  | [[Thymol (drug)]] 5 µM |  | -1.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | CST telomere replication complex component 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:8,224,815-8,248,058 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22170, AAF132; previously C17orf68 |
| Gene groups (HGNC) | CST complex |
| Reactome | 7 pathways, smallest: Telomere C-strand synthesis initiation; Polymerase switching on the C-strand of the telomere; Telomere C-strand (Lagging Strand) Synthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2NKJ3](https://www.uniprot.org/uniprotkb/Q2NKJ3) (CST complex subunit CTC1):

> Component of the CST complex proposed to act as a specialized replication factor promoting DNA replication under conditions of replication stress or natural replication barriers such as the telomere duplex. The CST complex binds single-stranded DNA with high affinity in a sequence-independent manner, while isolated subunits bind DNA with low affinity by themselves. Initially the CST complex has been proposed to protect telomeres from DNA degradation. However, the CST complex has been shown to …

**Summary**, from NCBI Gene [80169](https://www.ncbi.nlm.nih.gov/gene/80169):

> This gene encodes a component of the CST complex. This complex plays an essential role in protecting telomeres from degradation. This protein also forms a heterodimer with the CST complex subunit STN1 to form the enzyme alpha accessory factor. This enzyme regulates DNA replication. Mutations in this gene are the cause of cerebroretinal microangiopathy with calcifications and cysts. Alternate splicing results in both coding and non-coding variants. [provided by RefSeq, Mar 2012]

**Accessions** — [HGNC:26169](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26169) · Entrez [80169](https://www.ncbi.nlm.nih.gov/gene/80169) · UniProt [Q2NKJ3](https://www.uniprot.org/uniprotkb/Q2NKJ3) · Ensembl [ENSG00000178971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178971)

## Data

Gene col 10981: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10981); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10981, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10981]; `tensor/DDL_lfc|DDL_z.npy` [10981]; `embed/gene_vectors.npy` [10981]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10981 or target_col == 10981). Every well: [[CTC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
