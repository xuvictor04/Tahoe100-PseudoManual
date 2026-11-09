---
symbol: "RPL10"
type: "gene"
col: 7178
ensembl_id: "ENSG00000147403"
name: "ribosomal protein L10"
location: "Xq28"
module: 20
arm: "+"
pooled_cpm: 41.46
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# RPL10

*ribosomal protein L10* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.98× (z +9.4, q 4e-18, up in 38 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.10× (z +5.3, q 9e-06, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.773× (z -5.0, q 3e-04, down in 26 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (H4 0.155×, A-427 0.368×, SK-MEL-2 0.397×); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.182×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C-33 A 0.132×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL18A]] (+0.85, fdr 7e-06), [[RPS18]] (+0.81, fdr 7e-06), [[EEF1A1]] (+0.79, fdr 7e-06); moves opposite to [[CROCCP2-1]] (-0.67, fdr 7e-06), [[ERVK3-1]] (-0.66, fdr 7e-06), [[PIGBOS1]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7178.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +9.4 | 4e-18 | 38/45 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +8.0 | 3e-13 | 36/43 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +7.4 | 3e-11 | 8/48 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +7.1 | 2e-10 | 31/39 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.68×** | +7.1 | 2e-10 | 39/46 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.10×** | +5.3 | 9e-06 | 32/48 (RKO, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.10×** | +5.3 | 9e-06 | 37/49 (KATO III, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +4.2 | 0.002 | 17/35 (HOP62, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.002 | 23/48 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.003 | 26/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.9 | 0.006 | 19/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +3.7 | 0.009 | 21/48 (NCI-H1792, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.4 | 0.030 | 16/48 (NCI-H2347, Panc 03.27, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.071 | 18/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.093 | 14/48 (SNU-423, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7178.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (H4 0.155×, A-427 0.368×, SK-MEL-2 0.397×); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.182×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C-33 A 0.132×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.773×** | -5.0 | 3e-04 | 26/47 (H4, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.750×** | -3.9 | 0.022 | 29/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 0.786× | -3.3 | 0.14 | 19/48 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.779× | -3.3 | 0.14 | 18/47 (H4, SW 900, …) | inconsistent across doses |  |
| [[Ornidazole (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.792× | -3.2 | 0.16 | 16/48 (NCI-H2030, SW480, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.797× | -3.1 | 0.17 | 17/48 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses |  |
| [[Acetohexamide (drug)]] 5 µM |  | 0.854× | -3.1 | 0.17 | 13/48 (SW 1088, BT-474, …) | top dose only | position effect removed |
| [[Dapagliflozin (drug)]] 0.05 µM |  | 0.801× | -3.0 | 0.17 | 14/48 (SW480, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7178. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 54.2 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 3.41× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +8.9) | — |
| [[LoVo (line)]] | wt | 51.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.46× (z +11.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 42.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 40.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.59× (z +12.4) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 48.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.397× (z -9.5) |
| [[A-172 (line)]] | wt | 33.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.25× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 36.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -10.2) |
| [[C-33 A (line)]] | alt | 31.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 45.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -14.9) |
| [[NCI-H2347 (line)]] | alt | 39.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 39.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7178), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL18A]] | +0.85 | +0.76 / +0.83 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS18]] | +0.81 | +0.77 / +0.81 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[EEF1A1]] | +0.79 | +0.75 / +0.82 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 977 |
| [[ANKRD30BL]] | +0.79 | +0.72 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[EEF1A1P5]] | +0.76 | +0.71 / +0.77 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation |
| [[HFM1]] | +0.76 | +0.58 / +0.76 | both halves | 8e-06 | **novel candidate** |
| [[RPS3A]] | +0.76 | +0.70 / +0.76 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL4]] | +0.76 | +0.71 / +0.77 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL3]] | +0.75 | +0.76 / +0.76 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPSA]] | +0.73 | +0.70 / +0.71 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL29]] | +0.72 | +0.80 / +0.63 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 998 |
| [[EOLA2]] | +0.69 | +0.73 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP2-1]] | -0.67 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[ERVK3-1]] | -0.66 | -0.64 / -0.67 | both halves | 7e-06 |  |
| [[PIGBOS1]] | -0.66 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[CEBPZ]] | -0.64 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[ZNF503]] | -0.63 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[PPP1R12A]] | -0.60 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[TOPORS]] | -0.60 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[EID2]] | -0.60 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[MRPS18C]] | -0.59 | -0.57 / -0.63 | both halves | 9e-06 | STRING 601 |
| [[PRPF38B]] | -0.58 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[LARP7]] | -0.58 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[MRPL46]] | -0.57 | -0.45 / -0.66 | both halves | 3e-05 | STRING 767 |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.703). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-28.8, -25.4); signed map (-21.6, -34.3). **Vector** length 91.3, 22.0% of its response variance represented; |z| ≥ 3 in 691 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosomal scanning and start codon recognition* (reactome, mean cos +0.64 to 6); *Translation initiation complex formation* (reactome, mean cos +0.64 to 6); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.64 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.0 | +3.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.0 | +7.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.4 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +0.2 |
|  | [[Erlotinib (drug)]] 5 µM |  | +2.3 | +0.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +5.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | -1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +1.6 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -2.4 | -3.1 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -2.3 | -0.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.2 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -0.8 |
|  | [[Thymol (drug)]] 5 µM |  | -2.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:154,389,955-154,409,168 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NOV, QM, DXS648E, DXS648, FLJ23544, L10, uL16 |
| Gene groups (HGNC) | L ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P27635](https://www.uniprot.org/uniprotkb/P27635) (Large ribosomal subunit protein uL16):

> Component of the large ribosomal subunit. Plays a role in the formation of actively translating ribosomes. May play a role in the embryonic brain development.

**Summary**, from NCBI Gene [6134](https://www.ncbi.nlm.nih.gov/gene/6134):

> This gene encodes a ribosomal protein that is a component of the 60S ribosome subunit. The related protein in chicken can bind to c-Jun and can repress c-Jun-mediated transcriptional activation. Some studies have detected an association between variation in this gene and autism spectrum disorders, though others do not detect this relationship. There are multiple pseudogenes of this gene dispersed throughout the genome. Alternative splicing results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:10298](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10298) · Entrez [6134](https://www.ncbi.nlm.nih.gov/gene/6134) · UniProt [P27635](https://www.uniprot.org/uniprotkb/P27635) · Ensembl [ENSG00000147403](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147403)

## Data

Gene col 7178: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7178); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7178, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7178]; `tensor/DDL_lfc|DDL_z.npy` [7178]; `embed/gene_vectors.npy` [7178]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7178 or target_col == 7178). Every well: [[RPL10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
